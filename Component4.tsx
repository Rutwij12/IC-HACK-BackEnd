function TransformationCanvas() {
  const [matrix, setMatrix] = useState([[1, 0], [0, 1]]);
  const [shape, setShape] = useState([
    {x: 50, y: 50},
    {x: 150, y: 50}, 
    {x: 150, y: 150},
    {x: 50, y: 150}
  ]);

  const canvasRef = useRef(null);
  
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, 400, 400);
    
    // Draw original shape
    ctx.beginPath();
    ctx.strokeStyle = '#0066cc';
    ctx.moveTo(shape[0].x, shape[0].y);
    shape.forEach(point => ctx.lineTo(point.x, point.y));
    ctx.closePath();
    ctx.stroke();
    
    // Draw transformed shape
    ctx.beginPath(); 
    ctx.strokeStyle = '#003366';
    const transformedShape = shape.map(point => ({
      x: matrix[0][0] * point.x + matrix[0][1] * point.y,
      y: matrix[1][0] * point.x + matrix[1][1] * point.y
    }));
    
    ctx.moveTo(transformedShape[0].x, transformedShape[0].y);
    transformedShape.forEach(point => ctx.lineTo(point.x, point.y));
    ctx.closePath();
    ctx.stroke();
    
  }, [matrix, shape]);

  const handleMatrixChange = (row, col, value) => {
    const newMatrix = [...matrix];
    newMatrix[row][col] = parseFloat(value);
    setMatrix(newMatrix);
  };

  return (
    <div style={{fontFamily: 'Arial'}}>
      <h2 style={{color: '#003366', marginBottom: '20px'}}>
        Matrix Transformation Visualizer
      </h2>
      
      <div style={{marginBottom: '20px'}}>
        <div style={{color: '#0066cc', marginBottom: '10px'}}>
          Transformation Matrix:
        </div>
        <div style={{display: 'grid', gridTemplateColumns: '100px 100px', gap: '5px'}}>
          <input 
            type="number"
            value={matrix[0][0]}
            onChange={(e) => handleMatrixChange(0, 0, e.target.value)}
            style={{width: '80px'}}
          />
          <input
            type="number" 
            value={matrix[0][1]}
            onChange={(e) => handleMatrixChange(0, 1, e.target.value)}
            style={{width: '80px'}}
          />
          <input
            type="number"
            value={matrix[1][0]} 
            onChange={(e) => handleMatrixChange(1, 0, e.target.value)}
            style={{width: '80px'}}
          />
          <input
            type="number"
            value={matrix[1][1]}
            onChange={(e) => handleMatrixChange(1, 1, e.target.value)}
            style={{width: '80px'}}
          />
        </div>
      </div>

      <canvas
        ref={canvasRef}
        width={400}
        height={400}
        style={{
          border: '1px solid #0066cc',
          backgroundColor: '#f5f8fc'
        }}
      />
      
      <div style={{color: '#0066cc', marginTop: '10px', fontSize: '14px'}}>
        Blue: Original Shape
        <br/>
        Navy: Transformed Shape
      </div>
    </div>
  );
}