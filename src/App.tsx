import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function QuickIntroText() {
  return (
    <div style={{
      fontFamily: 'Arial',
      color: '#FF8533',
      padding: '20px',
      maxWidth: '800px',
      margin: '0 auto'
    }}>
      <h2 style={{
        fontSize: '28px',
        color: '#FF6600',
        marginBottom: '20px'
      }}>
        What is Integration?
      </h2>

      <div style={{
        fontSize: '18px',
        lineHeight: '1.6',
        color: '#FF944D'
      }}>
        <p>
          Integration is a fundamental concept in calculus that helps us find the total amount
          of a quantity over an interval. Think of it as adding up infinitely many infinitely
          small pieces to find a total.
        </p>

        <h3 style={{
          fontSize: '22px',
          color: '#FF751A',
          marginTop: '20px',
          marginBottom: '15px'
        }}>
          Real World Applications
        </h3>

        <p>
          We use integration in countless real-world scenarios:
        </p>

        <ul style={{color: '#FF944D', marginLeft: '20px'}}>
          <li>Calculating the total distance traveled from speed</li>
          <li>Finding the volume of irregular shapes</li>
          <li>Computing the total energy consumption over time</li>
          <li>Determining the center of mass of objects</li>
          <li>Analyzing probability distributions in statistics</li>
        </ul>

        <p style={{marginTop: '15px'}}>
          Whether you're an engineer designing buildings, a physicist studying motion,
          or an economist analyzing market trends, integration provides the tools to
          understand how quantities accumulate and change over time or space.
        </p>
      </div>
    </div>
  );
}
function BasicFormulaDisplay() {
  return (
    <div style={{
      fontFamily: 'Arial',
      color: '#FF8C00',
      padding: '20px',
      textAlign: 'center'
    }}>
      <h2 style={{
        fontSize: '24px',
        color: '#FFA500',
        marginBottom: '15px'
      }}>
        Basic Integration Formula Structure
      </h2>
      
      <div style={{
        fontSize: '60px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '10px'
      }}>
        <span style={{
          fontFamily: 'Times New Roman',
          fontSize: '80px',
          color: '#FF7F50'
        }}>
          ∫
        </span>
        
        <span style={{
          fontSize: '40px',
          color: '#FFA07A'
        }}>
          f(x) dx
        </span>
        
        <span style={{
          fontSize: '40px',
          color: '#FF8C00'
        }}>
          = F(x) + C
        </span>
      </div>
      
      <p style={{
        fontSize: '16px',
        color: '#FF7F50',
        marginTop: '20px'
      }}>
        Where F(x) is the antiderivative of f(x) and C is the constant of integration
      </p>
    </div>
  );
}
function AreaUnderCurveAnimation() {
  const [points, setPoints] = React.useState(10);
  const [showArea, setShowArea] = React.useState(false);
  const canvasRef = React.useRef(null);

  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.clearRect(0, 0, width, height);

    // Draw axes
    ctx.beginPath();
    ctx.strokeStyle = '#ff9933';
    ctx.moveTo(50, height - 50);
    ctx.lineTo(width - 50, height - 50); // x-axis
    ctx.moveTo(50, height - 50);
    ctx.lineTo(50, 50); // y-axis
    ctx.stroke();

    // Draw curve (parabola)
    ctx.beginPath();
    ctx.strokeStyle = '#ff6600';
    ctx.moveTo(50, height - 50);
    
    for(let x = 0; x <= width - 100; x++) {
      const y = 100 * Math.sin(x * 0.02) + 150;
      ctx.lineTo(x + 50, height - y);
    }
    ctx.stroke();

    // Draw rectangles under curve
    if (showArea) {
      ctx.fillStyle = 'rgba(255, 153, 51, 0.3)';
      const dx = (width - 100) / points;
      
      for(let i = 0; i < points; i++) {
        const x = i * dx;
        const y = 100 * Math.sin(x * 0.02) + 150;
        ctx.fillRect(
          x + 50,
          height - 50,
          dx,
          -y + 50
        );
      }
    }

  }, [points, showArea]);

  return (
    <div style={{fontFamily: 'Arial'}}>
      <h2 style={{color: '#cc5200', fontSize: '24px'}}>Area Under Curve Visualization</h2>
      <div style={{marginBottom: '20px'}}>
        <label style={{color: '#ff751a', marginRight: '10px'}}>
          Number of rectangles:
          <input 
            type="range" 
            min="1" 
            max="100" 
            value={points}
            onChange={(e) => setPoints(parseInt(e.target.value))}
          />
          {points}
        </label>
        <button
          style={{
            marginLeft: '20px',
            backgroundColor: '#ff751a',
            border: 'none',
            padding: '8px 16px',
            borderRadius: '4px',
            color: 'white',
            cursor: 'pointer'
          }}
          onClick={() => setShowArea(!showArea)}
        >
          {showArea ? 'Hide Area' : 'Show Area'}
        </button>
      </div>
      <canvas
        ref={canvasRef}
        width={600}
        height={400}
        style={{border: '2px solid #ff751a', borderRadius: '8px'}}
      />
      <p style={{color: '#ff751a', marginTop: '20px'}}>
        This visualization shows how integration can be approximated by summing the areas of rectangles under a curve. 
        Adjust the slider to change the number of rectangles and see how the approximation becomes more accurate.
      </p>
    </div>
  );
}
function IntegrationTypesGrid() {
  const integrationTypes = [
    {
      title: "API Integration",
      description: "Direct communication between systems using REST or GraphQL APIs"
    },
    {
      title: "Webhook Integration", 
      description: "Event-driven integration using HTTP callbacks"
    },
    {
      title: "File-based Integration",
      description: "Exchange of data through file transfers (CSV, XML, JSON)"
    },
    {
      title: "Database Integration",
      description: "Direct database connections and synchronization"
    },
    {
      title: "Message Queue",
      description: "Asynchronous communication using message brokers"
    },
    {
      title: "SDK Integration",
      description: "Using software development kits for native integration"
    }
  ];

  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px'
    }}>
      <h1 style={{
        color: '#FF8C00',
        fontSize: '2em',
        marginBottom: '30px'
      }}>
        Integration Types
      </h1>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
        gap: '20px'
      }}>
        {integrationTypes.map((type, index) => (
          <div key={index} style={{
            padding: '20px',
            border: '2px solid #FFA500',
            borderRadius: '8px',
            backgroundColor: '#FFF8DC'
          }}>
            <h3 style={{
              color: '#FF4500',
              marginBottom: '10px',
              fontSize: '1.2em'
            }}>
              {type.title}
            </h3>
            <p style={{
              color: '#FF8C00',
              fontSize: '0.9em',
              lineHeight: '1.4'
            }}>
              {type.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
function RealWorldExamplesCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0);

  const examples = [
    {
      title: "Architecture & Engineering",
      text: "Integration helps calculate load-bearing capacities of curved structures like bridges and domes"
    },
    {
      title: "Economics", 
      text: "Finding total revenue by integrating marginal revenue curves over time"
    },
    {
      title: "Physics",
      text: "Calculating work done by varying forces by integrating force over distance"
    },
    {
      title: "Biology",
      text: "Population growth modeling using integration of growth rate functions"
    }
  ];

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === examples.length - 1 ? 0 : prevIndex + 1
    );
  };

  const prevSlide = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? examples.length - 1 : prevIndex - 1
    );
  };

  return (
    <div style={{
      fontFamily: 'Arial',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      padding: '20px',
      backgroundColor: '#FFF5EB'
    }}>
      <h2 style={{
        color: '#FF8C00',
        fontSize: '24px',
        marginBottom: '20px'
      }}>
        Real World Applications
      </h2>

      <div style={{
        position: 'relative',
        width: '80%',
        height: '200px',
        backgroundColor: '#FFE4CC',
        borderRadius: '10px',
        padding: '20px',
        margin: '20px 0'
      }}>
        <h3 style={{
          color: '#FF7F24',
          fontSize: '20px',
          marginBottom: '10px'
        }}>
          {examples[currentIndex].title}
        </h3>
        <p style={{
          color: '#FF8C69',
          fontSize: '16px'
        }}>
          {examples[currentIndex].text}
        </p>
      </div>

      <div style={{
        display: 'flex',
        gap: '20px'
      }}>
        <button 
          onClick={prevSlide}
          style={{
            backgroundColor: '#FFA500',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '5px',
            color: 'white',
            cursor: 'pointer'
          }}
        >
          Previous
        </button>
        <button 
          onClick={nextSlide}
          style={{
            backgroundColor: '#FFA500',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '5px',
            color: 'white',
            cursor: 'pointer'
          }}
        >
          Next
        </button>
      </div>
    </div>
  );
}
function KeyPointsSummary() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      padding: '20px',
      maxWidth: '800px',
      margin: '0 auto'
    },
    title: {
      fontSize: '28px',
      color: '#FF8C00',
      marginBottom: '20px'
    },
    list: {
      listStyleType: 'circle',
      paddingLeft: '25px'
    },
    listItem: {
      color: '#FFA500',
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '12px'
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Key Integration Concepts</h2>
      <ul style={styles.list}>
        <li style={styles.listItem}>
          Always validate input data before processing to ensure data integrity
        </li>
        <li style={styles.listItem}>
          Implement proper error handling and logging mechanisms
        </li>
        <li style={styles.listItem}>
          Use asynchronous operations for better performance and scalability
        </li>
        <li style={styles.listItem}>
          Maintain consistent data formats across all integration points
        </li>
        <li style={styles.listItem}>
          Implement retry mechanisms for failed operations
        </li>
        <li style={styles.listItem}>
          Follow security best practices and encrypt sensitive data
        </li>
        <li style={styles.listItem}>
          Document all integration endpoints and their requirements
        </li>
        <li style={styles.listItem}>
          Monitor integration performance and set up alerts
        </li>
        <li style={styles.listItem}>
          Version your APIs to maintain backward compatibility
        </li>
        <li style={styles.listItem}>
          Regular testing of integration points to ensure reliability
        </li>
      </ul>
    </div>
  );
}

function App() {
  return (
    <div>
      <QuickIntroText />
      <div style={{ marginBottom: '2rem' }} />
      <BasicFormulaDisplay />
      <div style={{ marginBottom: '2rem' }} />
      <AreaUnderCurveAnimation />
      <div style={{ marginBottom: '2rem' }} />
      <IntegrationTypesGrid />
      <div style={{ marginBottom: '2rem' }} />
      <RealWorldExamplesCarousel />
      <div style={{ marginBottom: '2rem' }} />
      <KeyPointsSummary />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;