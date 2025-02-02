function GeometricTransformationDemo() {
  const [angle, setAngle] = React.useState(0);
  const [scale, setScale] = React.useState(1);
  const [showEigenvectors, setShowEigenvectors] = React.useState(true);

  const canvasRef = React.useRef(null);

  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw coordinate axes
    ctx.strokeStyle = '#FFA500';
    ctx.beginPath();
    ctx.moveTo(0, centerY);
    ctx.lineTo(canvas.width, centerY);
    ctx.moveTo(centerX, 0);
    ctx.lineTo(centerX, canvas.height);
    ctx.stroke();

    // Draw transformed unit vectors
    const transformedX = [
      Math.cos(angle * Math.PI / 180) * scale * 50,
      Math.sin(angle * Math.PI / 180) * scale * 50
    ];
    const transformedY = [
      -Math.sin(angle * Math.PI / 180) * scale * 50,
      Math.cos(angle * Math.PI / 180) * scale * 50
    ];

    // Draw transformed vectors
    ctx.strokeStyle = '#FF8C00';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + transformedX[0], centerY + transformedX[1]);
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + transformedY[0], centerY + transformedY[1]);
    ctx.stroke();

    // Draw eigenvectors if enabled
    if (showEigenvectors) {
      ctx.strokeStyle = '#FFA07A';
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(centerX - 50, centerY - 50);
      ctx.lineTo(centerX + 50, centerY + 50);
      ctx.moveTo(centerX - 50, centerY + 50);
      ctx.lineTo(centerX + 50, centerY - 50);
      ctx.stroke();
      ctx.setLineDash([]);
    }
  }, [angle, scale, showEigenvectors]);

  return (
    <div style={{ fontFamily: 'Arial', color: '#FF8C00' }}>
      <h2 style={{ fontSize: '24px', color: '#FFA500' }}>
        Geometric Transformation Demo
      </h2>
      
      <div style={{ marginBottom: '20px' }}>
        <canvas
          ref={canvasRef}
          width={400}
          height={400}
          style={{ border: '1px solid #FFA500' }}
        />
      </div>

      <div style={{ marginBottom: '10px' }}>
        <label style={{ marginRight: '10px' }}>
          Rotation Angle:
          <input
            type="range"
            min="0"
            max="360"
            value={angle}
            onChange={(e) => setAngle(Number(e.target.value))}
          />
          {angle}°
        </label>
      </div>

      <div style={{ marginBottom: '10px' }}>
        <label style={{ marginRight: '10px' }}>
          Scale:
          <input
            type="range"
            min="0.1"
            max="3"
            step="0.1"
            value={scale}
            onChange={(e) => setScale(Number(e.target.value))}
          />
          {scale.toFixed(1)}x
        </label>
      </div>

      <div>
        <label>
          <input
            type="checkbox"
            checked={showEigenvectors}
            onChange={(e) => setShowEigenvectors(e.target.checked)}
          />
          Show Eigenvectors
        </label>
      </div>
    </div>
  );
}