function TrigCircleVisualizer() {
  const [angle, setAngle] = React.useState(0);
  const [isDragging, setIsDragging] = React.useState(false);
  const canvasRef = React.useRef(null);

  const size = 300;
  const radius = 120;
  const center = size / 2;

  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, size, size);
    
    // Draw main circle
    ctx.beginPath();
    ctx.strokeStyle = '#ffa500';
    ctx.lineWidth = 2;
    ctx.arc(center, center, radius, 0, 2 * Math.PI);
    ctx.stroke();

    // Draw axes
    ctx.beginPath();
    ctx.strokeStyle = '#ffb732';
    ctx.moveTo(center - radius - 10, center);
    ctx.lineTo(center + radius + 10, center);
    ctx.moveTo(center, center - radius - 10);
    ctx.lineTo(center, center + radius + 10);
    ctx.stroke();

    // Calculate point on circle
    const x = center + radius * Math.cos(angle);
    const y = center - radius * Math.sin(angle);

    // Draw angle line
    ctx.beginPath();
    ctx.strokeStyle = '#ff8c00';
    ctx.moveTo(center, center);
    ctx.lineTo(x, y);
    ctx.stroke();

    // Draw sine line
    ctx.beginPath();
    ctx.strokeStyle = '#ffd700';
    ctx.setLineDash([5, 5]);
    ctx.moveTo(x, y);
    ctx.lineTo(x, center);
    ctx.stroke();
    ctx.setLineDash([]);

    // Draw cosine line
    ctx.beginPath();
    ctx.strokeStyle = '#ff4500';
    ctx.setLineDash([5, 5]);
    ctx.moveTo(x, y);
    ctx.lineTo(center, y);
    ctx.stroke();
    ctx.setLineDash([]);

  }, [angle]);

  const handleMouseDown = (e) => {
    setIsDragging(true);
    updateAngle(e);
  };

  const handleMouseMove = (e) => {
    if (isDragging) {
      updateAngle(e);
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const updateAngle = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left - center;
    const y = e.clientY - rect.top - center;
    setAngle(Math.atan2(-y, x));
  };

  return (
    <div style={{ fontFamily: 'Arial' }}>
      <h2 style={{ color: '#ff8c00', fontSize: '24px' }}>Unit Circle Visualizer</h2>
      <div>
        <canvas
          ref={canvasRef}
          width={size}
          height={size}
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onMouseLeave={handleMouseUp}
          style={{ cursor: 'pointer' }}
        />
      </div>
      <div style={{ color: '#ffa500', marginTop: '20px' }}>
        <p>Angle: {(angle * 180 / Math.PI).toFixed(1)}°</p>
        <p style={{ color: '#ffd700' }}>Sine: {Math.sin(angle).toFixed(3)}</p>
        <p style={{ color: '#ff4500' }}>Cosine: {Math.cos(angle).toFixed(3)}</p>
      </div>
    </div>
  );
}