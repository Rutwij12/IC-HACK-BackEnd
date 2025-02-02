function TheTheoremVisual() {
  const [angle, setAngle] = React.useState(45);
  const [isAnimating, setIsAnimating] = React.useState(false);

  const calculateTriangleDimensions = (angleInDegrees) => {
    const a = Math.cos(angleInDegrees * Math.PI / 180) * 100;
    const b = Math.sin(angleInDegrees * Math.PI / 180) * 100;
    const c = Math.sqrt(a * a + b * b);
    return { a, b, c };
  };

  const dimensions = calculateTriangleDimensions(angle);

  const handleSliderChange = (e) => {
    setAngle(e.target.value);
  };

  const toggleAnimation = () => {
    setIsAnimating(!isAnimating);
  };

  React.useEffect(() => {
    let animationFrame;
    if (isAnimating) {
      let currentAngle = angle;
      const animate = () => {
        currentAngle = (currentAngle + 1) % 90;
        setAngle(currentAngle);
        animationFrame = requestAnimationFrame(animate);
      };
      animationFrame = requestAnimationFrame(animate);
    }
    return () => cancelAnimationFrame(animationFrame);
  }, [isAnimating]);

  return (
    <div style={{ fontFamily: 'Arial', padding: '20px' }}>
      <h2 style={{ color: '#FF8C00', marginBottom: '20px' }}>
        Interactive Pythagorean Theorem
      </h2>
      
      <div style={{ position: 'relative', width: '300px', height: '300px' }}>
        <svg width="300" height="300">
          {/* Main triangle */}
          <path
            d={`M 50 250 L ${50 + dimensions.a} 250 L 50 ${250 - dimensions.b} Z`}
            fill="none"
            stroke="#FFA500"
            strokeWidth="2"
          />
          
          {/* Squares on each side */}
          <path
            d={`M 50 250 L 50 ${250 - dimensions.b} 
                L ${50 - dimensions.b} ${250 - dimensions.b} 
                L ${50 - dimensions.b} 250 Z`}
            fill="#FFE4B5"
            opacity="0.6"
          />
          
          <path
            d={`M ${50 + dimensions.a} 250 
                L ${50 + dimensions.a} ${250 + dimensions.a}
                L 50 ${250 + dimensions.a} 
                L 50 250 Z`}
            fill="#FFA07A"
            opacity="0.6"
          />
          
          <path
            d={`M 50 ${250 - dimensions.b} 
                L ${50 + dimensions.a} 250
                L ${50 + dimensions.a + dimensions.b} ${250 - dimensions.b}
                L ${50 + dimensions.b} ${250 - dimensions.a - dimensions.b} Z`}
            fill="#FFD700"
            opacity="0.6"
          />
        </svg>
      </div>

      <div style={{ marginTop: '20px', color: '#FF8C00' }}>
        <p>Angle: {angle}°</p>
        <input
          type="range"
          min="15"
          max="75"
          value={angle}
          onChange={handleSliderChange}
          style={{ width: '200px' }}
        />
      </div>

      <button
        onClick={toggleAnimation}
        style={{
          marginTop: '10px',
          padding: '8px 16px',
          backgroundColor: '#FFA500',
          border: 'none',
          borderRadius: '4px',
          color: 'white',
          cursor: 'pointer'
        }}
      >
        {isAnimating ? 'Stop Animation' : 'Start Animation'}
      </button>

      <div style={{ marginTop: '20px', color: '#FF8C00' }}>
        <p>a² + b² = c²</p>
        <p>
          {Math.round(dimensions.a * dimensions.a)} + {Math.round(dimensions.b * dimensions.b)} = {Math.round(dimensions.c * dimensions.c)}
        </p>
      </div>
    </div>
  );
}