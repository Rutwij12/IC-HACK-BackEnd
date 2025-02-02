function AreaUnderCurveAnimation() {
  const [points, setPoints] = React.useState(10);
  const [showArea, setShowArea] = React.useState(false);
  const canvasRef = React.useRef(null);

  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    // Draw axes
    ctx.beginPath();
    ctx.strokeStyle = '#ff9933';
    ctx.moveTo(50, height - 50);
    ctx.lineTo(width - 50, height - 50); // x-axis
    ctx.moveTo(50, height - 50);
    ctx.lineTo(50, 50); // y-axis
    ctx.stroke();

    // Draw curve (parabola)
    ctx.beginPath();
    ctx.strokeStyle = '#ff6600';
    ctx.moveTo(50, height - 50);
    
    for(let x = 0; x <= width - 100; x++) {
      const y = 100 * Math.sin(x * 0.02) + 150;
      ctx.lineTo(x + 50, height - y);
    }
    ctx.stroke();

    // Draw rectangles under curve
    if (showArea) {
      ctx.fillStyle = 'rgba(255, 153, 51, 0.3)';
      const dx = (width - 100) / points;
      
      for(let i = 0; i < points; i++) {
        const x = i * dx;
        const y = 100 * Math.sin(x * 0.02) + 150;
        ctx.fillRect(
          x + 50,
          height - 50,
          dx,
          -y + 50
        );
      }
    }

  }, [points, showArea]);

  return (
    <div style={{fontFamily: 'Arial'}}>
      <h2 style={{color: '#cc5200', fontSize: '24px'}}>Area Under Curve Visualization</h2>
      <div style={{marginBottom: '20px'}}>
        <label style={{color: '#ff751a', marginRight: '10px'}}>
          Number of rectangles:
          <input 
            type="range" 
            min="1" 
            max="100" 
            value={points}
            onChange={(e) => setPoints(parseInt(e.target.value))}
          />
          {points}
        </label>
        <button
          style={{
            marginLeft: '20px',
            backgroundColor: '#ff751a',
            border: 'none',
            padding: '8px 16px',
            borderRadius: '4px',
            color: 'white',
            cursor: 'pointer'
          }}
          onClick={() => setShowArea(!showArea)}
        >
          {showArea ? 'Hide Area' : 'Show Area'}
        </button>
      </div>
      <canvas
        ref={canvasRef}
        width={600}
        height={400}
        style={{border: '2px solid #ff751a', borderRadius: '8px'}}
      />
      <p style={{color: '#ff751a', marginTop: '20px'}}>
        This visualization shows how integration can be approximated by summing the areas of rectangles under a curve. 
        Adjust the slider to change the number of rectangles and see how the approximation becomes more accurate.
      </p>
    </div>
  );
}