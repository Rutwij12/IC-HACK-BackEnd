import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function EigenvectorDefinitionText() {
  return (
    <div style={{
      fontFamily: 'Arial',
      maxWidth: '800px',
      margin: '20px',
      color: '#CC7000'
    }}>
      <h2 style={{
        fontSize: '28px',
        color: '#FF8C00',
        marginBottom: '20px'
      }}>
        Understanding Eigenvectors - The Simple Way
      </h2>

      <p style={{
        fontSize: '18px',
        lineHeight: '1.6',
        marginBottom: '15px'
      }}>
        Think of an eigenvector like a special arrow that keeps pointing in the same direction even when you perform a transformation on it. Imagine you have a blanket, and you're stretching or squishing it - an eigenvector would be like a line drawn on that blanket that maintains its direction, even though it might get longer or shorter.
      </p>

      <p style={{
        fontSize: '18px',
        lineHeight: '1.6',
        marginBottom: '15px'
      }}>
        Here's another way to think about it: Picture a merry-go-round. Most points on the merry-go-round move in circles when it spins, but the center point stays in place - it just rotates. This center point is like an eigenvector of the spinning transformation.
      </p>

      <p style={{
        fontSize: '18px',
        lineHeight: '1.6'
      }}>
        In everyday terms, eigenvectors are like the "natural" directions of a transformation - they're the special directions where the transformation's effect is simplest, just stretching or shrinking along that direction, nothing more complicated.
      </p>
    </div>
  );
}
function InteractiveMatrix() {
  const [angle, setAngle] = React.useState(0);
  const [scale, setScale] = React.useState(1);
  
  // Calculate matrix transformation based on angle and scale
  const transformMatrix = {
    a: Math.cos(angle) * scale,
    b: -Math.sin(angle) * scale, 
    c: Math.sin(angle) * scale,
    d: Math.cos(angle) * scale
  };

  // Original vector coordinates
  const vector = {x: 50, y: 0};
  
  // Apply transformation
  const transformedVector = {
    x: transformMatrix.a * vector.x + transformMatrix.b * vector.y,
    y: transformMatrix.c * vector.x + transformMatrix.d * vector.y
  };

  const styles = {
    container: {
      fontFamily: 'Arial',
      padding: '20px',
      color: '#FF8C00'
    },
    title: {
      fontSize: '24px',
      color: '#FF4500',
      marginBottom: '20px'
    },
    canvas: {
      border: '1px solid #FFA500',
      backgroundColor: '#FFF8DC',
      margin: '20px 0'
    },
    controls: {
      display: 'flex',
      flexDirection: 'column',
      gap: '10px',
      marginBottom: '20px'
    },
    label: {
      color: '#FF7F50'
    }
  };

  const drawVector = (ctx, x, y, color) => {
    ctx.beginPath();
    ctx.moveTo(150, 150);
    ctx.lineTo(150 + x, 150 - y);
    ctx.strokeStyle = color;
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(150 + x, 150 - y, 3, 0, 2 * Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
  };

  React.useEffect(() => {
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, 300, 300);
    
    // Draw grid
    ctx.strokeStyle = '#FFE4B5';
    for(let i = 0; i <= 300; i += 30) {
      ctx.beginPath();
      ctx.moveTo(i, 0);
      ctx.lineTo(i, 300);
      ctx.moveTo(0, i);
      ctx.lineTo(300, i);
      ctx.stroke();
    }
    
    // Draw original vector
    drawVector(ctx, vector.x, vector.y, '#FF8C00');
    
    // Draw transformed vector
    drawVector(ctx, transformedVector.x, transformedVector.y, '#FF4500');
    
  }, [angle, scale, transformedVector]);

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Matrix Transformation Visualization</h2>
      
      <div style={styles.controls}>
        <div>
          <label style={styles.label}>Rotation Angle: </label>
          <input 
            type="range" 
            min="0" 
            max={2 * Math.PI} 
            step="0.1"
            value={angle}
            onChange={(e) => setAngle(Number(e.target.value))}
          />
          {Math.round(angle * 180 / Math.PI)}°
        </div>
        
        <div>
          <label style={styles.label}>Scale: </label>
          <input 
            type="range"
            min="0.1"
            max="2"
            step="0.1"
            value={scale}
            onChange={(e) => setScale(Number(e.target.value))}
          />
          {scale.toFixed(1)}x
        </div>
      </div>

      <canvas 
        id="matrixCanvas"
        width={300}
        height={300}
        style={styles.canvas}
      />
      
      <p style={{color: '#FF8C00'}}>
        Orange vector: Original vector<br/>
        Red vector: Transformed vector
      </p>
    </div>
  );
}
function GeometricTransformationDemo() {
  const [angle, setAngle] = React.useState(0);
  const [scale, setScale] = React.useState(1);
  const [showEigenvectors, setShowEigenvectors] = React.useState(true);

  const canvasRef = React.useRef(null);

  React.useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw coordinate axes
    ctx.strokeStyle = '#FFA500';
    ctx.beginPath();
    ctx.moveTo(0, centerY);
    ctx.lineTo(canvas.width, centerY);
    ctx.moveTo(centerX, 0);
    ctx.lineTo(centerX, canvas.height);
    ctx.stroke();

    // Draw transformed unit vectors
    const transformedX = [
      Math.cos(angle * Math.PI / 180) * scale * 50,
      Math.sin(angle * Math.PI / 180) * scale * 50
    ];
    const transformedY = [
      -Math.sin(angle * Math.PI / 180) * scale * 50,
      Math.cos(angle * Math.PI / 180) * scale * 50
    ];

    // Draw transformed vectors
    ctx.strokeStyle = '#FF8C00';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + transformedX[0], centerY + transformedX[1]);
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + transformedY[0], centerY + transformedY[1]);
    ctx.stroke();

    // Draw eigenvectors if enabled
    if (showEigenvectors) {
      ctx.strokeStyle = '#FFA07A';
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(centerX - 50, centerY - 50);
      ctx.lineTo(centerX + 50, centerY + 50);
      ctx.moveTo(centerX - 50, centerY + 50);
      ctx.lineTo(centerX + 50, centerY - 50);
      ctx.stroke();
      ctx.setLineDash([]);
    }
  }, [angle, scale, showEigenvectors]);

  return (
    <div style={{ fontFamily: 'Arial', color: '#FF8C00' }}>
      <h2 style={{ fontSize: '24px', color: '#FFA500' }}>
        Geometric Transformation Demo
      </h2>
      
      <div style={{ marginBottom: '20px' }}>
        <canvas
          ref={canvasRef}
          width={400}
          height={400}
          style={{ border: '1px solid #FFA500' }}
        />
      </div>

      <div style={{ marginBottom: '10px' }}>
        <label style={{ marginRight: '10px' }}>
          Rotation Angle:
          <input
            type="range"
            min="0"
            max="360"
            value={angle}
            onChange={(e) => setAngle(Number(e.target.value))}
          />
          {angle}°
        </label>
      </div>

      <div style={{ marginBottom: '10px' }}>
        <label style={{ marginRight: '10px' }}>
          Scale:
          <input
            type="range"
            min="0.1"
            max="3"
            step="0.1"
            value={scale}
            onChange={(e) => setScale(Number(e.target.value))}
          />
          {scale.toFixed(1)}x
        </label>
      </div>

      <div>
        <label>
          <input
            type="checkbox"
            checked={showEigenvectors}
            onChange={(e) => setShowEigenvectors(e.target.checked)}
          />
          Show Eigenvectors
        </label>
      </div>
    </div>
  );
}
function RealWorldExamplesText() {
  const containerStyle = {
    fontFamily: 'Arial, sans-serif',
    color: '#D35400',
    maxWidth: '800px',
    margin: '20px',
    lineHeight: '1.6'
  }

  const titleStyle = {
    color: '#E67E22',
    fontSize: '28px',
    marginBottom: '20px',
    fontWeight: 'bold'
  }

  const sectionTitleStyle = {
    color: '#F39C12',
    fontSize: '20px',
    marginTop: '15px',
    marginBottom: '10px'
  }

  const paragraphStyle = {
    fontSize: '16px',
    marginBottom: '15px'
  }

  return (
    <div style={containerStyle}>
      <h1 style={titleStyle}>Real-World Applications of Eigenvectors</h1>
      
      <h2 style={sectionTitleStyle}>Physics Applications</h2>
      <p style={paragraphStyle}>
        In quantum mechanics, eigenvectors are fundamental in describing the stable states of quantum systems. They represent the possible states of particles, while their corresponding eigenvalues represent the observable properties like energy levels. For instance, the electron orbitals in atoms are eigenvectors of the quantum mechanical Hamiltonian operator.
      </p>
      <p style={paragraphStyle}>
        In structural mechanics, eigenvectors describe the natural modes of vibration in buildings and bridges. Engineers use this information to design structures that can withstand earthquakes and other forms of mechanical stress.
      </p>

      <h2 style={sectionTitleStyle}>Computer Graphics Applications</h2>
      <p style={paragraphStyle}>
        In computer graphics and image processing, eigenvectors are used for facial recognition systems. Principal Component Analysis (PCA), which relies on eigenvectors, helps reduce the dimensionality of facial images while retaining their key characteristics.
      </p>
      <p style={paragraphStyle}>
        3D graphics applications use eigenvectors for character animation and object deformation. They help determine principal directions of stretching and compression, making animations more realistic and computationally efficient.
      </p>

      <h2 style={sectionTitleStyle}>Data Science Applications</h2>
      <p style={paragraphStyle}>
        Search engines like Google use eigenvectors in their PageRank algorithm to rank web pages. The algorithm treats web pages as nodes in a network and uses eigenvector centrality to determine their importance and relevance.
      </p>
      <p style={paragraphStyle}>
        In machine learning, eigenvectors are crucial for dimensionality reduction techniques, helping to compress large datasets while preserving their most important features and patterns.
      </p>
    </div>
  )
}
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
function BasicMathNotationGuide() {
  return (
    <div style={{ 
      fontFamily: 'Arial, sans-serif',
      color: '#D35400',
      padding: '20px',
      maxWidth: '800px'
    }}>
      <h1 style={{ 
        fontSize: '28px',
        color: '#E67E22',
        marginBottom: '20px'
      }}>
        Basic Guide to Eigenvector Notation
      </h1>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Definition
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          An eigenvector is a non-zero vector that changes only by a scalar factor when a linear transformation is applied.
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Basic Notation
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          The standard notation for eigenvectors is: Av = λv
          Where:
          - A is a square matrix
          - v is an eigenvector
          - λ (lambda) is the eigenvalue
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Written Form
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          When writing about eigenvectors, we typically say:
          "v is an eigenvector of A with eigenvalue λ"
        </p>
      </div>

      <div style={{ marginBottom: '24px' }}>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Important Properties
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          1. Eigenvectors can only be found for square matrices
          2. A matrix may have multiple eigenvector-eigenvalue pairs
          3. Eigenvectors corresponding to different eigenvalues are linearly independent
          4. The zero vector is never an eigenvector
        </p>
      </div>

      <div>
        <h2 style={{ 
          fontSize: '22px',
          color: '#F39C12',
          marginBottom: '12px'
        }}>
          Common Usage
        </h2>
        <p style={{ lineHeight: '1.6' }}>
          Eigenvectors are typically written in column form and are often normalized (made to have length 1).
          They are commonly used in:
          - Principal Component Analysis (PCA)
          - Diagonalization
          - Quantum Mechanics
          - Computer Graphics
        </p>
      </div>
    </div>
  );
}

function App() {
  return (
    <div>
      <EigenvectorDefinitionText />
      <div style={{ marginBottom: '2rem' }} />
      <InteractiveMatrix />
      <div style={{ marginBottom: '2rem' }} />
      <GeometricTransformationDemo />
      <div style={{ marginBottom: '2rem' }} />
      <RealWorldExamplesText />
      <div style={{ marginBottom: '2rem' }} />
      <VectorPlayground />
      <div style={{ marginBottom: '2rem' }} />
      <BasicMathNotationGuide />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;