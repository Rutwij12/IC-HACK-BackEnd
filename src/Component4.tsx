function WavePatternDemo() {
  const [angle, setAngle] = React.useState(0);
  const [isPlaying, setIsPlaying] = React.useState(false);
  
  const canvasRef = React.useRef(null);
  
  React.useEffect(() => {
    let animationId;
    
    const animate = () => {
      if (isPlaying) {
        setAngle(prev => (prev + 2) % 360);
        animationId = requestAnimationFrame(animate);
      }
    };
    
    if (isPlaying) {
      animationId = requestAnimationFrame(animate);
    }
    
    return () => cancelAnimationFrame(animationId);
  }, [isPlaying]);
  
  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const centerX = 150;
    const centerY = 150;
    const radius = 50;
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw circle
    ctx.beginPath();
    ctx.strokeStyle = '#FFA500';
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.stroke();
    
    // Draw rotating point
    const radians = angle * Math.PI / 180;
    const pointX = centerX + radius * Math.cos(radians);
    const pointY = centerY + radius * Math.sin(radians);
    
    ctx.fillStyle = '#FF8C00';
    ctx.beginPath();
    ctx.arc(pointX, pointY, 5, 0, 2 * Math.PI);
    ctx.fill();
    
    // Draw sine wave
    ctx.beginPath();
    ctx.moveTo(300, pointY);
    ctx.strokeStyle = '#FFA500';
    for (let i = 0; i <= 360; i++) {
      const x = 300 + i;
      const y = centerY + radius * Math.sin((i - angle) * Math.PI / 180);
      ctx.lineTo(x, y);
    }
    ctx.stroke();
    
    // Draw cosine wave
    ctx.beginPath();
    ctx.moveTo(pointX, 300);
    ctx.strokeStyle = '#FF4500';
    for (let i = 0; i <= 360; i++) {
      const x = centerX + radius * Math.cos((i - angle) * Math.PI / 180);
      const y = 300 + i;
      ctx.lineTo(x, y);
    }
    ctx.stroke();
    
    // Draw projection lines
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(pointX, pointY);
    ctx.lineTo(300, pointY);
    ctx.moveTo(pointX, pointY);
    ctx.lineTo(pointX, 300);
    ctx.stroke();
    ctx.setLineDash([]);
    
  }, [angle]);

  return (
    <div style={{ fontFamily: 'Arial', color: '#FF8C00' }}>
      <h2 style={{ fontSize: '24px', color: '#FF4500' }}>Wave Pattern Demonstration</h2>
      <div>
        <canvas 
          ref={canvasRef}
          width={700}
          height={500}
          style={{ border: '1px solid #FFA500' }}
        />
      </div>
      <button 
        onClick={() => setIsPlaying(!isPlaying)}
        style={{
          backgroundColor: '#FFA500',
          color: 'white',
          border: 'none',
          padding: '10px 20px',
          margin: '10px',
          borderRadius: '5px',
          cursor: 'pointer'
        }}
      >
        {isPlaying ? 'Pause' : 'Play'}
      </button>
      <div style={{ fontSize: '14px', marginTop: '10px' }}>
        Orange: Sine Wave | Dark Orange: Cosine Wave
      </div>
    </div>
  );
}