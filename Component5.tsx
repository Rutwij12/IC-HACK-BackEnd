function InteractiveGridDemo() {
  const [matrix, setMatrix] = useState([
    [1, 0],
    [0, 1]
  ]);
  
  const [points, setPoints] = useState([
    {x: 100, y: 100},
    {x: 200, y: 100},
    {x: 100, y: 200},
    {x: 200, y: 200}
  ]);

  const transformPoint = (point) => {
    const newX = point.x * matrix[0][0] + point.y * matrix[0][1];
    const newY = point.x * matrix[1][0] + point.y * matrix[1][1];
    return {x: newX, y: newY};
  };

  const handleMatrixChange = (row, col, value) => {
    const newMatrix = [...matrix];
    newMatrix[row][col] = parseFloat(value) || 0;
    setMatrix(newMatrix);
    
    // Transform all points with new matrix
    const newPoints = points.map(point => transformPoint(point));
    setPoints(newPoints);
  };

  const styles = {
    container: {
      fontFamily: 'Arial',
      padding: '20px',
      color: '#0066cc'
    },
    title: {
      fontSize: '24px',
      color: '#003366',
      marginBottom: '20px'
    },
    grid: {
      position: 'relative',
      width: '400px',
      height: '400px',
      border: '1px solid #0066cc',
      margin: '20px 0'
    },
    point: {
      position: 'absolute',
      width: '8px',
      height: '8px',
      backgroundColor: '#0066cc',
      borderRadius: '50%',
      transform: 'translate(-50%, -50%)'
    },
    matrixInput: {
      display: 'grid',
      gridTemplateColumns: 'repeat(2, 60px)',
      gap: '10px',
      marginBottom: '20px'
    },
    input: {
      width: '50px',
      padding: '5px',
      border: '1px solid #0066cc'
    },
    subtitle: {
      fontSize: '18px',
      color: '#004d99',
      marginBottom: '10px'
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Matrix Transformation Visualizer</h1>
      
      <h2 style={styles.subtitle}>Input Matrix Values</h2>
      <div style={styles.matrixInput}>
        <input 
          type="number"
          value={matrix[0][0]}
          onChange={(e) => handleMatrixChange(0, 0, e.target.value)}
          style={styles.input}
        />
        <input 
          type="number"
          value={matrix[0][1]}
          onChange={(e) => handleMatrixChange(0, 1, e.target.value)}
          style={styles.input}
        />
        <input 
          type="number"
          value={matrix[1][0]}
          onChange={(e) => handleMatrixChange(1, 0, e.target.value)}
          style={styles.input}
        />
        <input 
          type="number"
          value={matrix[1][1]}
          onChange={(e) => handleMatrixChange(1, 1, e.target.value)}
          style={styles.input}
        />
      </div>

      <h2 style={styles.subtitle}>Transformation Result</h2>
      <div style={styles.grid}>
        {points.map((point, index) => (
          <div
            key={index}
            style={{
              ...styles.point,
              left: `${point.x}px`,
              top: `${point.y}px`
            }}
          />
        ))}
      </div>
    </div>
  );
}