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