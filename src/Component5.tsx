function LegacyImpactWheel() {
  const [selectedField, setSelectedField] = useState(null);
  const [rotation, setRotation] = useState(0);

  const fields = [
    { name: 'Mathematics', color: '#FFA500', description: 'Theorem and number theory foundations' },
    { name: 'Music', color: '#FF8C00', description: 'Harmonic ratios and musical scales' },
    { name: 'Architecture', color: '#FFA07A', description: 'Sacred geometry and proportions' },
    { name: 'Philosophy', color: '#FFD700', description: 'Mysticism and metaphysics' },
    { name: 'Astronomy', color: '#FF7F50', description: 'Celestial harmony and orbits' },
    { name: 'Science', color: '#FF4500', description: 'Scientific method foundations' }
  ];

  const handleFieldClick = (field) => {
    setSelectedField(field);
  };

  const handleWheelClick = () => {
    setRotation(rotation + 60);
    setSelectedField(null);
  };

  return (
    <div style={{ 
      fontFamily: 'Arial',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '20px',
      padding: '20px'
    }}>
      <h2 style={{ color: '#FF8C00', fontSize: '24px' }}>Pythagorean Legacy Impact</h2>
      
      <div style={{ 
        position: 'relative',
        width: '400px',
        height: '400px',
        cursor: 'pointer'
      }} onClick={handleWheelClick}>
        {fields.map((field, index) => {
          const angle = (index * 60 + rotation) * (Math.PI / 180);
          const centerX = 200 + 150 * Math.cos(angle);
          const centerY = 200 + 150 * Math.sin(angle);

          return (
            <div
              key={field.name}
              onClick={(e) => {
                e.stopPropagation();
                handleFieldClick(field);
              }}
              style={{
                position: 'absolute',
                left: centerX - 50,
                top: centerY - 50,
                width: '100px',
                height: '100px',
                borderRadius: '50%',
                backgroundColor: field.color,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'white',
                fontWeight: 'bold',
                transition: 'transform 0.5s ease',
                transform: `rotate(${rotation}deg)`,
                cursor: 'pointer'
              }}
            >
              {field.name}
            </div>
          );
        })}
      </div>

      {selectedField && (
        <div style={{
          backgroundColor: selectedField.color,
          padding: '20px',
          borderRadius: '10px',
          color: 'white',
          maxWidth: '300px',
          textAlign: 'center'
        }}>
          <h3>{selectedField.name}</h3>
          <p>{selectedField.description}</p>
        </div>
      )}

      <p style={{ color: '#FF8C00', fontSize: '14px', textAlign: 'center' }}>
        Click on a field to learn more or click the wheel to rotate
      </p>
    </div>
  );
}