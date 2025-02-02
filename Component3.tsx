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