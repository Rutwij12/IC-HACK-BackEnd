import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function BiographyIntro() {
  return (
    <div style={{
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '0 auto',
      padding: '20px'
    }}>
      <h1 style={{
        fontSize: '2.5em',
        color: '#FF8C00',
        marginBottom: '20px'
      }}>
        Pythagoras of Samos
      </h1>
      
      <p style={{
        fontSize: '1.2em',
        lineHeight: '1.6',
        color: '#FF7F50',
        marginBottom: '15px'
      }}>
        One of the most influential and enigmatic figures in ancient Greek philosophy and mathematics, Pythagoras (c. 570-495 BCE) left an indelible mark on human thought that resonates to this day.
      </p>

      <p style={{
        fontSize: '1.1em',
        lineHeight: '1.6',
        color: '#FFA07A',
        marginBottom: '15px'
      }}>
        Born on the island of Samos, Pythagoras founded a philosophical and religious school in Croton, Italy, where he developed his famous mathematical theories and cultivated a devoted following. His teachings extended far beyond mathematics into music, astronomy, and metaphysics.
      </p>

      <p style={{
        fontSize: '1.1em',
        lineHeight: '1.6',
        color: '#FFA07A'
      }}>
        While he is most commonly known for the Pythagorean theorem, his influence spans much broader - from his belief in the mathematical nature of reality to his teachings on the immortality of the soul. His ideas would later influence great thinkers like Plato and continue to shape our understanding of mathematics and philosophy.
      </p>
    </div>
  );
}
function TimelineBanner() {
  const [selectedEvent, setSelectedEvent] = useState(null);

  const events = [
    {
      year: "570 BCE",
      title: "Birth",
      details: "Born on the island of Samos, Greece"
    },
    {
      year: "535 BCE", 
      title: "Migration to Italy",
      details: "Established his school in Croton"
    },
    {
      year: "532 BCE",
      title: "Pythagoras' Theorem",
      details: "Formalized the relationship between sides of right triangles"
    },
    {
      year: "520 BCE",
      title: "Music Theory",
      details: "Discovered mathematical ratios in musical harmonies"
    },
    {
      year: "495 BCE",
      title: "Death",
      details: "Died in Metapontum, Italy"
    }
  ];

  const timelineStyles = {
    container: {
      padding: "20px",
      fontFamily: "Arial",
      position: "relative"
    },
    line: {
      height: "4px",
      backgroundColor: "#FFA500",
      width: "100%",
      margin: "50px 0"
    },
    events: {
      display: "flex",
      justifyContent: "space-between",
      position: "relative"
    },
    event: {
      cursor: "pointer",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      width: "120px"
    },
    dot: {
      width: "20px",
      height: "20px",
      borderRadius: "50%",
      backgroundColor: "#FF8C00",
      margin: "10px 0"
    },
    year: {
      color: "#FF6600",
      fontWeight: "bold"
    },
    selectedEvent: {
      position: "absolute",
      top: "100px",
      left: "50%",
      transform: "translateX(-50%)",
      backgroundColor: "#FFF3E0",
      padding: "15px",
      borderRadius: "8px",
      boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
      color: "#FF8C00",
      textAlign: "center"
    }
  };

  return (
    <div style={timelineStyles.container}>
      <h2 style={{color: "#FF4500", fontSize: "24px", textAlign: "center"}}>
        Pythagoras Timeline
      </h2>
      <div style={timelineStyles.line} />
      <div style={timelineStyles.events}>
        {events.map((event, index) => (
          <div 
            key={index}
            style={timelineStyles.event}
            onClick={() => setSelectedEvent(event)}
          >
            <div style={timelineStyles.dot} />
            <span style={timelineStyles.year}>{event.year}</span>
          </div>
        ))}
      </div>
      {selectedEvent && (
        <div style={timelineStyles.selectedEvent}>
          <h3 style={{color: "#FF4500", margin: "0 0 10px 0"}}>
            {selectedEvent.title}
          </h3>
          <p style={{color: "#FF8C00", margin: 0}}>
            {selectedEvent.details}
          </p>
        </div>
      )}
    </div>
  );
}
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
function NumberMysticismText() {
  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '800px',
      margin: '0 auto'
    }}>
      <h1 style={{
        color: '#FF8C00',
        fontSize: '2.5em',
        marginBottom: '20px'
      }}>
        The Sacred Mathematics of Pythagoras
      </h1>

      <div style={{
        color: '#FF7F50',
        fontSize: '1.1em',
        lineHeight: '1.6'
      }}>
        <p>
          Pythagoras, the ancient Greek philosopher and mathematician, believed numbers were far more than mere mathematical concepts - they were the very essence of everything in the universe. His mystical approach to numbers transformed mathematics into a spiritual practice.
        </p>

        <p>
          To Pythagoras, each number held deep symbolic meaning. The number One represented unity and the divine source of all things. Two symbolized duality and the material world. Three was considered perfect harmony, while Four represented earthly elements and justice. The number Ten was seen as the most sacred, containing the sum of the first four numbers (1+2+3+4=10).
        </p>

        <p>
          The Pythagoreans even attributed personalities and qualities to numbers. Odd numbers were considered masculine and yang, while even numbers were feminine and yin. Some numbers were thought to embody certain virtues - Seven was associated with wisdom and Five with marriage.
        </p>

        <p>
          Perhaps most famously, Pythagoras discovered the mathematical relationships in musical harmonies, leading him to declare that "everything is arranged according to number." This revelation strengthened his conviction that numbers were the key to understanding the divine architecture of the cosmos.
        </p>

        <p>
          His followers, known as the Pythagoreans, formed a semi-religious sect dedicated to studying numbers and their mystical properties. They took oaths of secrecy and lived by strict rules, treating mathematics as a path to spiritual enlightenment rather than just a practical tool.
        </p>
      </div>
    </div>
  );
}
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
function MusicMathDiagram() {
  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '800px',
      margin: '0 auto'
    }}>
      <h2 style={{
        color: '#FF7F00',
        fontSize: '28px',
        marginBottom: '20px'
      }}>
        Pythagorean Musical Ratios
      </h2>
      
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        marginBottom: '40px'
      }}>
        <div style={{
          border: '2px solid #FFB366',
          padding: '15px',
          borderRadius: '8px',
          width: '45%'
        }}>
          <h3 style={{color: '#FF8C1A', marginBottom: '10px'}}>
            String Length Ratios
          </h3>
          <svg width="200" height="120">
            <line x1="20" y1="20" x2="180" y2="20" stroke="#FF9933" strokeWidth="2"/>
            <text x="85" y="15" style={{fill: '#FF9933'}}>1:1 (Unison)</text>
            
            <line x1="20" y1="60" x2="100" y2="60" stroke="#FF9933" strokeWidth="2"/>
            <text x="85" y="55" style={{fill: '#FF9933'}}>2:1 (Octave)</text>
            
            <line x1="20" y1="100" x2="140" y2="100" stroke="#FF9933" strokeWidth="2"/>
            <text x="85" y="95" style={{fill: '#FF9933'}}>3:2 (Fifth)</text>
          </svg>
        </div>

        <div style={{
          border: '2px solid #FFB366',
          padding: '15px', 
          borderRadius: '8px',
          width: '45%'
        }}>
          <h3 style={{color: '#FF8C1A', marginBottom: '10px'}}>
            Sound Wave Patterns
          </h3>
          <svg width="200" height="120">
            <path d="M 10 60 Q 52.5 20, 95 60 T 180 60" 
                  fill="none" 
                  stroke="#FF9933" 
                  strokeWidth="2"/>
            <path d="M 10 60 Q 35 100, 60 60 T 110 60" 
                  fill="none" 
                  stroke="#FF9933" 
                  strokeWidth="2"/>
          </svg>
        </div>
      </div>

      <p style={{
        color: '#FF944D',
        fontSize: '16px',
        lineHeight: '1.5',
        textAlign: 'center'
      }}>
        Pythagoras discovered that pleasant musical intervals correspond to simple whole-number ratios.
        When string lengths have ratios of 2:1, they produce an octave; 3:2 creates a perfect fifth.
      </p>
    </div>
  );
}

function App() {
  return (
    <div>
      <BiographyIntro />
      <div style={{ marginBottom: '2rem' }} />
      <TimelineBanner />
      <div style={{ marginBottom: '2rem' }} />
      <TheTheoremVisual />
      <div style={{ marginBottom: '2rem' }} />
      <NumberMysticismText />
      <div style={{ marginBottom: '2rem' }} />
      <LegacyImpactWheel />
      <div style={{ marginBottom: '2rem' }} />
      <MusicMathDiagram />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;