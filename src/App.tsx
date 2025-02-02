import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function TrigCircleVisualizer() {
  const [angle, setAngle] = React.useState(0);
  const [isDragging, setIsDragging] = React.useState(false);
  const canvasRef = React.useRef(null);

  const size = 300;
  const radius = 120;
  const center = size / 2;

  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, size, size);
    
    // Draw main circle
    ctx.beginPath();
    ctx.strokeStyle = '#ffa500';
    ctx.lineWidth = 2;
    ctx.arc(center, center, radius, 0, 2 * Math.PI);
    ctx.stroke();

    // Draw axes
    ctx.beginPath();
    ctx.strokeStyle = '#ffb732';
    ctx.moveTo(center - radius - 10, center);
    ctx.lineTo(center + radius + 10, center);
    ctx.moveTo(center, center - radius - 10);
    ctx.lineTo(center, center + radius + 10);
    ctx.stroke();

    // Calculate point on circle
    const x = center + radius * Math.cos(angle);
    const y = center - radius * Math.sin(angle);

    // Draw angle line
    ctx.beginPath();
    ctx.strokeStyle = '#ff8c00';
    ctx.moveTo(center, center);
    ctx.lineTo(x, y);
    ctx.stroke();

    // Draw sine line
    ctx.beginPath();
    ctx.strokeStyle = '#ffd700';
    ctx.setLineDash([5, 5]);
    ctx.moveTo(x, y);
    ctx.lineTo(x, center);
    ctx.stroke();
    ctx.setLineDash([]);

    // Draw cosine line
    ctx.beginPath();
    ctx.strokeStyle = '#ff4500';
    ctx.setLineDash([5, 5]);
    ctx.moveTo(x, y);
    ctx.lineTo(center, y);
    ctx.stroke();
    ctx.setLineDash([]);

  }, [angle]);

  const handleMouseDown = (e) => {
    setIsDragging(true);
    updateAngle(e);
  };

  const handleMouseMove = (e) => {
    if (isDragging) {
      updateAngle(e);
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const updateAngle = (e) => {
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left - center;
    const y = e.clientY - rect.top - center;
    setAngle(Math.atan2(-y, x));
  };

  return (
    <div style={{ fontFamily: 'Arial' }}>
      <h2 style={{ color: '#ff8c00', fontSize: '24px' }}>Unit Circle Visualizer</h2>
      <div>
        <canvas
          ref={canvasRef}
          width={size}
          height={size}
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onMouseLeave={handleMouseUp}
          style={{ cursor: 'pointer' }}
        />
      </div>
      <div style={{ color: '#ffa500', marginTop: '20px' }}>
        <p>Angle: {(angle * 180 / Math.PI).toFixed(1)}°</p>
        <p style={{ color: '#ffd700' }}>Sine: {Math.sin(angle).toFixed(3)}</p>
        <p style={{ color: '#ff4500' }}>Cosine: {Math.cos(angle).toFixed(3)}</p>
      </div>
    </div>
  );
}
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
function RealWorldExampleCards() {
  const examples = [
    {
      field: "Architecture",
      description: "Calculating roof angles and support beam placement. Architects use trigonometry to determine optimal roof pitches for drainage and load distribution.",
      icon: "🏛️"
    },
    {
      field: "Civil Engineering", 
      description: "Bridge design and construction. Engineers use trigonometric functions to calculate cable tensions and arch supports in bridge structures.",
      icon: "🌉"
    },
    {
      field: "Aviation",
      description: "Flight navigation and control. Pilots use trigonometry to calculate flight paths, angles of ascent/descent, and wind compensation.",
      icon: "✈️"
    },
    {
      field: "Marine Navigation",
      description: "Ship routing and positioning. Navigators use trigonometric calculations to determine bearings, distances and positions at sea.",
      icon: "🚢"
    },
    {
      field: "Game Development",
      description: "Character movement and collision detection. Game developers use trig to calculate realistic object motion and interactions.",
      icon: "🎮"
    },
    {
      field: "Music",
      description: "Sound wave analysis and synthesis. Audio engineers use trigonometric functions to process and create sound waves.",
      icon: "🎵"
    }
  ];

  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '1200px',
      margin: '0 auto'
    }}>
      <h2 style={{
        color: '#D35400',
        fontSize: '28px',
        marginBottom: '30px',
        textAlign: 'center'
      }}>
        Real-World Applications of Trigonometry
      </h2>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '20px',
        justifyContent: 'center'
      }}>
        {examples.map((example, index) => (
          <div key={index} style={{
            backgroundColor: '#FFF3E0',
            padding: '20px',
            borderRadius: '8px',
            boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
            transition: 'transform 0.2s',
            cursor: 'pointer',
            ':hover': {
              transform: 'translateY(-5px)'
            }
          }}>
            <div style={{
              fontSize: '40px',
              marginBottom: '10px',
              textAlign: 'center'
            }}>
              {example.icon}
            </div>
            <h3 style={{
              color: '#E67E22',
              fontSize: '20px',
              marginBottom: '10px'
            }}>
              {example.field}
            </h3>
            <p style={{
              color: '#D35400',
              fontSize: '16px',
              lineHeight: '1.5'
            }}>
              {example.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
function WavePatternDemo() {
  const [angle, setAngle] = React.useState(0);
  const [isPlaying, setIsPlaying] = React.useState(false);
  
  const canvasRef = React.useRef(null);
  
  React.useEffect(() => {
    let animationId;
    
    const animate = () => {
      if (isPlaying) {
        setAngle(prev => (prev + 2) % 360);
        animationId = requestAnimationFrame(animate);
      }
    };
    
    if (isPlaying) {
      animationId = requestAnimationFrame(animate);
    }
    
    return () => cancelAnimationFrame(animationId);
  }, [isPlaying]);
  
  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const centerX = 150;
    const centerY = 150;
    const radius = 50;
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw circle
    ctx.beginPath();
    ctx.strokeStyle = '#FFA500';
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.stroke();
    
    // Draw rotating point
    const radians = angle * Math.PI / 180;
    const pointX = centerX + radius * Math.cos(radians);
    const pointY = centerY + radius * Math.sin(radians);
    
    ctx.fillStyle = '#FF8C00';
    ctx.beginPath();
    ctx.arc(pointX, pointY, 5, 0, 2 * Math.PI);
    ctx.fill();
    
    // Draw sine wave
    ctx.beginPath();
    ctx.moveTo(300, pointY);
    ctx.strokeStyle = '#FFA500';
    for (let i = 0; i <= 360; i++) {
      const x = 300 + i;
      const y = centerY + radius * Math.sin((i - angle) * Math.PI / 180);
      ctx.lineTo(x, y);
    }
    ctx.stroke();
    
    // Draw cosine wave
    ctx.beginPath();
    ctx.moveTo(pointX, 300);
    ctx.strokeStyle = '#FF4500';
    for (let i = 0; i <= 360; i++) {
      const x = centerX + radius * Math.cos((i - angle) * Math.PI / 180);
      const y = 300 + i;
      ctx.lineTo(x, y);
    }
    ctx.stroke();
    
    // Draw projection lines
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(pointX, pointY);
    ctx.lineTo(300, pointY);
    ctx.moveTo(pointX, pointY);
    ctx.lineTo(pointX, 300);
    ctx.stroke();
    ctx.setLineDash([]);
    
  }, [angle]);

  return (
    <div style={{ fontFamily: 'Arial', color: '#FF8C00' }}>
      <h2 style={{ fontSize: '24px', color: '#FF4500' }}>Wave Pattern Demonstration</h2>
      <div>
        <canvas 
          ref={canvasRef}
          width={700}
          height={500}
          style={{ border: '1px solid #FFA500' }}
        />
      </div>
      <button 
        onClick={() => setIsPlaying(!isPlaying)}
        style={{
          backgroundColor: '#FFA500',
          color: 'white',
          border: 'none',
          padding: '10px 20px',
          margin: '10px',
          borderRadius: '5px',
          cursor: 'pointer'
        }}
      >
        {isPlaying ? 'Pause' : 'Play'}
      </button>
      <div style={{ fontSize: '14px', marginTop: '10px' }}>
        Orange: Sine Wave | Dark Orange: Cosine Wave
      </div>
    </div>
  );
}
function TrigRatiosExplainer() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#D35400'
    },
    title: {
      fontSize: '32px',
      color: '#E67E22',
      marginBottom: '24px'
    },
    section: {
      marginBottom: '20px'
    },
    sectionTitle: {
      fontSize: '24px',
      color: '#F39C12',
      marginBottom: '12px'
    },
    text: {
      fontSize: '16px',
      lineHeight: '1.6',
      color: '#E67E22'
    },
    mnemonic: {
      fontStyle: 'italic',
      color: '#F39C12',
      marginTop: '8px'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Understanding Trigonometric Ratios</h1>
      
      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Sine (sin)</h2>
        <p style={styles.text}>
          Sine is the ratio of the opposite side to the hypotenuse in a right triangle.
        </p>
        <p style={styles.mnemonic}>
          Remember: "SOH" - Sine equals Opposite over Hypotenuse
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Cosine (cos)</h2>
        <p style={styles.text}>
          Cosine is the ratio of the adjacent side to the hypotenuse in a right triangle.
        </p>
        <p style={styles.mnemonic}>
          Remember: "CAH" - Cosine equals Adjacent over Hypotenuse
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Tangent (tan)</h2>
        <p style={styles.text}>
          Tangent is the ratio of the opposite side to the adjacent side in a right triangle.
        </p>
        <p style={styles.mnemonic}>
          Remember: "TOA" - Tangent equals Opposite over Adjacent
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>SOHCAHTOA</h2>
        <p style={styles.text}>
          Put it all together and you get SOHCAHTOA - the classic mnemonic device for remembering all three ratios:
        </p>
        <p style={styles.mnemonic}>
          SOH - Sine = Opposite / Hypotenuse
          CAH - Cosine = Adjacent / Hypotenuse
          TOA - Tangent = Opposite / Adjacent
        </p>
      </div>
    </div>
  )
}
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

function App() {
  return (
    <div>
      <TrigCircleVisualizer />
      <div style={{ marginBottom: '2rem' }} />
      <AngleFundamentals />
      <div style={{ marginBottom: '2rem' }} />
      <RealWorldExampleCards />
      <div style={{ marginBottom: '2rem' }} />
      <WavePatternDemo />
      <div style={{ marginBottom: '2rem' }} />
      <TrigRatiosExplainer />
      <div style={{ marginBottom: '2rem' }} />
      <TriangleCalculator />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;