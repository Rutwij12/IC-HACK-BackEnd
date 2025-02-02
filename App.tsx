import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function MatrixBasicsText() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#1a365d'
    },
    title: {
      fontSize: '28px',
      color: '#2c5282',
      marginBottom: '20px'
    },
    subtitle: {
      fontSize: '22px',
      color: '#2b6cb0',
      marginTop: '20px',
      marginBottom: '12px'
    },
    paragraph: {
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '16px',
      color: '#2d3748'
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Understanding Matrix Multiplication</h1>

      <h2 style={styles.subtitle}>What is Matrix Multiplication?</h2>
      <p style={styles.paragraph}>
        Matrix multiplication is an operation that combines two matrices to create a new matrix. 
        Unlike regular multiplication, matrix multiplication involves a specific process of multiplying 
        and adding elements in a particular pattern.
      </p>

      <h2 style={styles.subtitle}>Basic Rules</h2>
      <p style={styles.paragraph}>
        To multiply two matrices, the number of columns in the first matrix must equal the number 
        of rows in the second matrix. The resulting matrix will have the same number of rows as 
        the first matrix and the same number of columns as the second matrix.
      </p>

      <h2 style={styles.subtitle}>The Process</h2>
      <p style={styles.paragraph}>
        Each element in the resulting matrix is calculated by taking a row from the first matrix 
        and a column from the second matrix. We multiply corresponding elements and add the products. 
        This process is repeated for each position in the resulting matrix.
      </p>

      <h2 style={styles.subtitle}>Key Properties</h2>
      <p style={styles.paragraph}>
        Matrix multiplication is not commutative, meaning A × B is not necessarily equal to B × A. 
        However, it is associative, meaning (A × B) × C equals A × (B × C). The identity matrix, 
        when multiplied with any matrix, returns the original matrix.
      </p>

      <h2 style={styles.subtitle}>Applications</h2>
      <p style={styles.paragraph}>
        Matrix multiplication is fundamental in many fields including computer graphics for transformations, 
        quantum mechanics for state changes, and machine learning for data transformations. It's also 
        essential in solving systems of linear equations and in various optimization problems.
      </p>
    </div>
  );
}
function TransformationExplainer() {
  const [selectedExample, setSelectedExample] = useState(0);
  const [showResult, setShowResult] = useState(false);

  const examples = [
    {
      matrix: [[2, 0], [0, 2]],
      vector: [1, 1],
      description: "Scale by 2 in both directions",
      result: [2, 2]
    },
    {
      matrix: [[0, -1], [1, 0]], 
      vector: [1, 0],
      description: "90 degree rotation",
      result: [0, 1]
    },
    {
      matrix: [[1, 1], [0, 1]],
      vector: [1, 0], 
      description: "Shear transformation",
      result: [1, 0]
    }
  ];

  const currentExample = examples[selectedExample];

  const styles = {
    container: {
      fontFamily: 'Arial',
      color: '#1a4b8c',
      padding: '20px'
    },
    title: {
      fontSize: '24px',
      color: '#0d3875',
      marginBottom: '20px'
    },
    description: {
      fontSize: '16px',
      marginBottom: '15px'
    },
    button: {
      backgroundColor: '#3474d4',
      color: 'white',
      border: 'none',
      padding: '8px 16px',
      borderRadius: '4px',
      margin: '5px',
      cursor: 'pointer'
    },
    matrix: {
      fontFamily: 'monospace',
      fontSize: '18px',
      margin: '10px 0'
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Matrix Transformations</h1>
      
      <div style={styles.description}>
        <p>Select different examples to see how matrices transform vectors:</p>
        
        <div>
          {examples.map((_, index) => (
            <button 
              key={index}
              style={styles.button}
              onClick={() => {
                setSelectedExample(index);
                setShowResult(false);
              }}
            >
              Example {index + 1}
            </button>
          ))}
        </div>

        <div style={{marginTop: '20px'}}>
          <h3 style={{color: '#2960a8'}}>Current Transform: {currentExample.description}</h3>
          
          <div style={styles.matrix}>
            Matrix: [
            {currentExample.matrix.map(row => `[${row.join(', ')}]`).join(', ')}
            ]
          </div>
          
          <div style={styles.matrix}>
            Vector: [{currentExample.vector.join(', ')}]
          </div>

          <button 
            style={styles.button}
            onClick={() => setShowResult(!showResult)}
          >
            {showResult ? 'Hide' : 'Show'} Result
          </button>

          {showResult && (
            <div style={styles.matrix}>
              Result: [{currentExample.result.join(', ')}]
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
function MatrixMultiplicationVisualizer() {
  const [step, setStep] = useState(0);
  const [showResult, setShowResult] = useState(false);
  
  const matrix1 = [[1, 2], [3, 4]];
  const matrix2 = [[5, 6], [7, 8]];
  const result = [[19, 22], [43, 50]];

  const getHighlightColor = (i, j, matrix) => {
    if (!showResult) {
      if (matrix === 1) {
        return step === i * 2 + j ? '#add8e6' : 'white';
      } else if (matrix === 2) {
        return step === j * 2 + i ? '#add8e6' : 'white';
      }
    }
    return 'white';
  };

  const renderMatrix = (matrix, id) => (
    <div style={{ display: 'inline-block', margin: '0 20px' }}>
      {matrix.map((row, i) => (
        <div key={i} style={{ display: 'flex' }}>
          {row.map((cell, j) => (
            <div
              key={j}
              style={{
                width: '40px',
                height: '40px',
                border: '1px solid #1e90ff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: getHighlightColor(i, j, id),
                fontFamily: 'Arial',
                transition: 'background-color 0.3s'
              }}
            >
              {cell}
            </div>
          ))}
        </div>
      ))}
    </div>
  );

  const handleNext = () => {
    if (step < 3) {
      setStep(step + 1);
    } else {
      setShowResult(true);
    }
  };

  const handleReset = () => {
    setStep(0);
    setShowResult(false);
  };

  return (
    <div style={{ textAlign: 'center', fontFamily: 'Arial' }}>
      <h2 style={{ color: '#0056b3' }}>Matrix Multiplication Visualizer</h2>
      <div style={{ margin: '20px' }}>
        {renderMatrix(matrix1, 1)}
        <span style={{ fontSize: '24px', color: '#1e90ff' }}>×</span>
        {renderMatrix(matrix2, 2)}
        <span style={{ fontSize: '24px', color: '#1e90ff' }}>=</span>
        {showResult && renderMatrix(result, 3)}
      </div>
      <div>
        {!showResult && (
          <div style={{ color: '#4682b4', marginBottom: '10px' }}>
            Step {step + 1}: Calculating element ({Math.floor(step/2) + 1}, {(step % 2) + 1})
          </div>
        )}
        <button
          onClick={handleNext}
          disabled={showResult}
          style={{
            padding: '8px 16px',
            backgroundColor: '#1e90ff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            marginRight: '10px',
            cursor: showResult ? 'not-allowed' : 'pointer'
          }}
        >
          Next Step
        </button>
        <button
          onClick={handleReset}
          style={{
            padding: '8px 16px',
            backgroundColor: '#4682b4',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Reset
        </button>
      </div>
    </div>
  );
}
function TransformationCanvas() {
  const [matrix, setMatrix] = useState([[1, 0], [0, 1]]);
  const [shape, setShape] = useState([
    {x: 50, y: 50},
    {x: 150, y: 50}, 
    {x: 150, y: 150},
    {x: 50, y: 150}
  ]);

  const canvasRef = useRef(null);
  
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, 400, 400);
    
    // Draw original shape
    ctx.beginPath();
    ctx.strokeStyle = '#0066cc';
    ctx.moveTo(shape[0].x, shape[0].y);
    shape.forEach(point => ctx.lineTo(point.x, point.y));
    ctx.closePath();
    ctx.stroke();
    
    // Draw transformed shape
    ctx.beginPath(); 
    ctx.strokeStyle = '#003366';
    const transformedShape = shape.map(point => ({
      x: matrix[0][0] * point.x + matrix[0][1] * point.y,
      y: matrix[1][0] * point.x + matrix[1][1] * point.y
    }));
    
    ctx.moveTo(transformedShape[0].x, transformedShape[0].y);
    transformedShape.forEach(point => ctx.lineTo(point.x, point.y));
    ctx.closePath();
    ctx.stroke();
    
  }, [matrix, shape]);

  const handleMatrixChange = (row, col, value) => {
    const newMatrix = [...matrix];
    newMatrix[row][col] = parseFloat(value);
    setMatrix(newMatrix);
  };

  return (
    <div style={{fontFamily: 'Arial'}}>
      <h2 style={{color: '#003366', marginBottom: '20px'}}>
        Matrix Transformation Visualizer
      </h2>
      
      <div style={{marginBottom: '20px'}}>
        <div style={{color: '#0066cc', marginBottom: '10px'}}>
          Transformation Matrix:
        </div>
        <div style={{display: 'grid', gridTemplateColumns: '100px 100px', gap: '5px'}}>
          <input 
            type="number"
            value={matrix[0][0]}
            onChange={(e) => handleMatrixChange(0, 0, e.target.value)}
            style={{width: '80px'}}
          />
          <input
            type="number" 
            value={matrix[0][1]}
            onChange={(e) => handleMatrixChange(0, 1, e.target.value)}
            style={{width: '80px'}}
          />
          <input
            type="number"
            value={matrix[1][0]} 
            onChange={(e) => handleMatrixChange(1, 0, e.target.value)}
            style={{width: '80px'}}
          />
          <input
            type="number"
            value={matrix[1][1]}
            onChange={(e) => handleMatrixChange(1, 1, e.target.value)}
            style={{width: '80px'}}
          />
        </div>
      </div>

      <canvas
        ref={canvasRef}
        width={400}
        height={400}
        style={{
          border: '1px solid #0066cc',
          backgroundColor: '#f5f8fc'
        }}
      />
      
      <div style={{color: '#0066cc', marginTop: '10px', fontSize: '14px'}}>
        Blue: Original Shape
        <br/>
        Navy: Transformed Shape
      </div>
    </div>
  );
}
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

function App() {
  return (
    <div>
      <MatrixBasicsText />
      <div style={{ marginBottom: '2rem' }} />
      <TransformationExplainer />
      <div style={{ marginBottom: '2rem' }} />
      <MatrixMultiplicationVisualizer />
      <div style={{ marginBottom: '2rem' }} />
      <TransformationCanvas />
      <div style={{ marginBottom: '2rem' }} />
      <InteractiveGridDemo />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;