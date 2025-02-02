function VectorPlayground() {
  const [vector, setVector] = useState({ x: 100, y: 100 });
  const [isDragging, setIsDragging] = useState(false);
  const [isEigenvector, setIsEigenvector] = useState(false);
  
  // Matrix transformation (example 2x2 matrix)
  const matrix = [
    [2, 1],
    [1, 2]
  ];

  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, 400, 400);
    
    // Draw coordinate system
    ctx.strokeStyle = '#ccc';
    ctx.beginPath();
    ctx.moveTo(200, 0);
    ctx.lineTo(200, 400);
    ctx.moveTo(0, 200);
    ctx.lineTo(400, 200);
    ctx.stroke();

    // Draw original vector
    ctx.strokeStyle = '#ff8c00';
    ctx.beginPath();
    ctx.moveTo(200, 200);
    ctx.lineTo(vector.x, vector.y);
    ctx.stroke();

    // Calculate transformed vector
    const vectorCoords = [vector.x - 200, vector.y - 200];
    const transformedVector = [
      matrix[0][0] * vectorCoords[0] + matrix[0][1] * vectorCoords[1],
      matrix[1][0] * vectorCoords[0] + matrix[1][1] * vectorCoords[1]
    ];

    // Draw transformed vector
    ctx.strokeStyle = '#ffa500';
    ctx.beginPath();
    ctx.moveTo(200, 200);
    ctx.lineTo(transformedVector[0] + 200, transformedVector[1] + 200);
    ctx.stroke();

    // Check if it's an eigenvector (approximately)
    const originalLength = Math.sqrt(vectorCoords[0]**2 + vectorCoords[1]**2);
    const transformedLength = Math.sqrt(transformedVector[0]**2 + transformedVector[1]**2);
    const dotProduct = vectorCoords[0] * transformedVector[0] + vectorCoords[1] * transformedVector[1];
    const angle = Math.acos(dotProduct / (originalLength * transformedLength));
    
    setIsEigenvector(angle < 0.1); // Allow small deviation
  }, [vector]);

  const handleMouseDown = (e) => {
    setIsDragging(true);
  };

  const handleMouseMove = (e) => {
    if (isDragging) {
      const rect = canvasRef.current.getBoundingClientRect();
      setVector({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
      });
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  return (
    <div style={{ fontFamily: 'Arial' }}>
      <h2 style={{ color: '#ff8c00', fontSize: '24px' }}>Vector Playground</h2>
      <p style={{ color: '#ff8c00' }}>
        Drag to create a vector. Orange shows original, darker orange shows transformed vector.
      </p>
      <canvas
        ref={canvasRef}
        width={400}
        height={400}
        style={{ border: '1px solid #ffd700', cursor: 'pointer' }}
        onMouseDown={handleMouseDown}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
        onMouseLeave={handleMouseUp}
      />
      <p style={{ color: '#ff8c00', marginTop: '10px' }}>
        {isEigenvector 
          ? "This appears to be an eigenvector!" 
          : "This is not an eigenvector."}
      </p>
    </div>
  );
}