function TriangleCalculator() {
  const [side1, setSide1] = React.useState('');
  const [side2, setSide2] = React.useState('');
  const [side3, setSide3] = React.useState('');
  const [angle1, setAngle1] = React.useState('');
  const [angle2, setAngle2] = React.useState('');
  const [angle3, setAngle3] = React.useState('');

  const calculateTriangle = () => {
    // Calculate missing angles using law of cosines
    if (side1 && side2 && side3) {
      const a = parseFloat(side1);
      const b = parseFloat(side2);
      const c = parseFloat(side3);
      
      const angleA = Math.acos((b*b + c*c - a*a)/(2*b*c)) * (180/Math.PI);
      const angleB = Math.acos((a*a + c*c - b*b)/(2*a*c)) * (180/Math.PI);
      const angleC = 180 - angleA - angleB;
      
      setAngle1(angleA.toFixed(1));
      setAngle2(angleB.toFixed(1));
      setAngle3(angleC.toFixed(1));
    }
  };

  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '500px',
      margin: '0 auto'
    }}>
      <h2 style={{
        color: '#FF8C00',
        fontSize: '24px',
        marginBottom: '20px'
      }}>
        Triangle Calculator
      </h2>

      <div style={{
        backgroundColor: '#FFF3E0',
        padding: '20px',
        borderRadius: '8px'
      }}>
        <div style={{marginBottom: '15px'}}>
          <label style={{color: '#E65100', display: 'block', marginBottom: '5px'}}>
            Side 1:
          </label>
          <input
            type="number"
            value={side1}
            onChange={(e) => setSide1(e.target.value)}
            style={{
              width: '100px',
              padding: '5px',
              border: '1px solid #FFB74D'
            }}
          />
        </div>

        <div style={{marginBottom: '15px'}}>
          <label style={{color: '#E65100', display: 'block', marginBottom: '5px'}}>
            Side 2:
          </label>
          <input
            type="number"
            value={side2}
            onChange={(e) => setSide2(e.target.value)}
            style={{
              width: '100px',
              padding: '5px',
              border: '1px solid #FFB74D'
            }}
          />
        </div>

        <div style={{marginBottom: '15px'}}>
          <label style={{color: '#E65100', display: 'block', marginBottom: '5px'}}>
            Side 3:
          </label>
          <input
            type="number"
            value={side3}
            onChange={(e) => setSide3(e.target.value)}
            style={{
              width: '100px',
              padding: '5px',
              border: '1px solid #FFB74D'
            }}
          />
        </div>

        <button
          onClick={calculateTriangle}
          style={{
            backgroundColor: '#FF9800',
            color: 'white',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Calculate Angles
        </button>

        {angle1 && angle2 && angle3 && (
          <div style={{
            marginTop: '20px',
            padding: '15px',
            backgroundColor: '#FFE0B2',
            borderRadius: '4px'
          }}>
            <h3 style={{color: '#E65100', fontSize: '18px', marginBottom: '10px'}}>
              Results:
            </h3>
            <p style={{color: '#F57C00', margin: '5px 0'}}>Angle 1: {angle1}°</p>
            <p style={{color: '#F57C00', margin: '5px 0'}}>Angle 2: {angle2}°</p>
            <p style={{color: '#F57C00', margin: '5px 0'}}>Angle 3: {angle3}°</p>
          </div>
        )}
      </div>
    </div>
  );
}