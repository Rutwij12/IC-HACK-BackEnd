function InteractiveMatrix() {
  const [angle, setAngle] = React.useState(0);
  const [scale, setScale] = React.useState(1);
  
  // Calculate matrix transformation based on angle and scale
  const transformMatrix = {
    a: Math.cos(angle) * scale,
    b: -Math.sin(angle) * scale, 
    c: Math.sin(angle) * scale,
    d: Math.cos(angle) * scale
  };

  // Original vector coordinates
  const vector = {x: 50, y: 0};
  
  // Apply transformation
  const transformedVector = {
    x: transformMatrix.a * vector.x + transformMatrix.b * vector.y,
    y: transformMatrix.c * vector.x + transformMatrix.d * vector.y
  };

  const styles = {
    container: {
      fontFamily: 'Arial',
      padding: '20px',
      color: '#FF8C00'
    },
    title: {
      fontSize: '24px',
      color: '#FF4500',
      marginBottom: '20px'
    },
    canvas: {
      border: '1px solid #FFA500',
      backgroundColor: '#FFF8DC',
      margin: '20px 0'
    },
    controls: {
      display: 'flex',
      flexDirection: 'column',
      gap: '10px',
      marginBottom: '20px'
    },
    label: {
      color: '#FF7F50'
    }
  };

  const drawVector = (ctx, x, y, color) => {
    ctx.beginPath();
    ctx.moveTo(150, 150);
    ctx.lineTo(150 + x, 150 - y);
    ctx.strokeStyle = color;
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(150 + x, 150 - y, 3, 0, 2 * Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
  };

  React.useEffect(() => {
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, 300, 300);
    
    // Draw grid
    ctx.strokeStyle = '#FFE4B5';
    for(let i = 0; i <= 300; i += 30) {
      ctx.beginPath();
      ctx.moveTo(i, 0);
      ctx.lineTo(i, 300);
      ctx.moveTo(0, i);
      ctx.lineTo(300, i);
      ctx.stroke();
    }
    
    // Draw original vector
    drawVector(ctx, vector.x, vector.y, '#FF8C00');
    
    // Draw transformed vector
    drawVector(ctx, transformedVector.x, transformedVector.y, '#FF4500');
    
  }, [angle, scale, transformedVector]);

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Matrix Transformation Visualization</h2>
      
      <div style={styles.controls}>
        <div>
          <label style={styles.label}>Rotation Angle: </label>
          <input 
            type="range" 
            min="0" 
            max={2 * Math.PI} 
            step="0.1"
            value={angle}
            onChange={(e) => setAngle(Number(e.target.value))}
          />
          {Math.round(angle * 180 / Math.PI)}°
        </div>
        
        <div>
          <label style={styles.label}>Scale: </label>
          <input 
            type="range"
            min="0.1"
            max="2"
            step="0.1"
            value={scale}
            onChange={(e) => setScale(Number(e.target.value))}
          />
          {scale.toFixed(1)}x
        </div>
      </div>

      <canvas 
        id="matrixCanvas"
        width={300}
        height={300}
        style={styles.canvas}
      />
      
      <p style={{color: '#FF8C00'}}>
        Orange vector: Original vector<br/>
        Red vector: Transformed vector
      </p>
    </div>
  );
}