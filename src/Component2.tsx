function AngleFundamentals() {
  const titleStyle = {
    fontFamily: 'Arial',
    fontSize: '28px',
    color: '#FF8C00',
    marginBottom: '20px'
  };

  const paragraphStyle = {
    fontFamily: 'Arial',
    fontSize: '16px',
    color: '#FFA500',
    lineHeight: '1.6',
    marginBottom: '15px'
  };

  const subtitleStyle = {
    fontFamily: 'Arial',
    fontSize: '20px',
    color: '#FF7F50',
    marginTop: '20px',
    marginBottom: '10px'
  };

  return (
    <div style={{padding: '20px'}}>
      <h1 style={titleStyle}>Understanding Angle Measurements</h1>
      
      <div style={paragraphStyle}>
        Angles can be measured in two primary ways: degrees and radians. Each has its own uses and advantages in mathematics and real-world applications.
      </div>

      <h2 style={subtitleStyle}>Degrees (°)</h2>
      <div style={paragraphStyle}>
        Degrees are the most common way to measure angles in everyday life. There are 360 degrees in a full circle.
        - A quarter turn = 90°
        - A half turn = 180°
        - A full turn = 360°
      </div>

      <h2 style={subtitleStyle}>Radians (rad)</h2>
      <div style={paragraphStyle}>
        Radians are the standard unit in advanced mathematics and physics. A radian is the angle made when you wrap the radius length around the circle's arc.
        - π radians = 180°
        - 2π radians = 360°
        - π/2 radians = 90°
      </div>

      <h2 style={subtitleStyle}>Common Conversions</h2>
      <div style={paragraphStyle}>
        To convert from degrees to radians: multiply by π/180
        To convert from radians to degrees: multiply by 180/π
      </div>

      <div style={paragraphStyle}>
        For example:
        - 45° = π/4 radians
        - 90° = π/2 radians
        - 30° = π/6 radians
      </div>
    </div>
  );
}