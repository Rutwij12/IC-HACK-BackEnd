function SetOperationsCalculator() {
  const [set1, setSet1] = React.useState(['a', 'b', 'c']);
  const [set2, setSet2] = React.useState(['b', 'c', 'd']);
  const [set1Input, setSet1Input] = React.useState('');
  const [set2Input, setSet2Input] = React.useState('');

  const updateSet = (input, setNum) => {
    const elements = input.split(',').map(el => el.trim()).filter(el => el);
    if (setNum === 1) {
      setSet1(elements);
    } else {
      setSet2(elements);
    }
  };

  const union = [...new Set([...set1, ...set2])];
  const intersection = set1.filter(item => set2.includes(item));
  const difference = set1.filter(item => !set2.includes(item));

  const styles = {
    container: {
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '600px',
      margin: '0 auto',
    },
    title: {
      fontSize: '24px',
      color: '#FF8C00',
      marginBottom: '20px',
    },
    input: {
      marginBottom: '15px',
      width: '100%',
      padding: '8px',
      border: '1px solid #FFA500',
    },
    setDisplay: {
      backgroundColor: '#FFF3E0',
      padding: '10px',
      marginBottom: '10px',
      borderRadius: '5px',
      color: '#E65100',
    },
    results: {
      marginTop: '20px',
      color: '#F57C00',
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Set Operations Calculator</h1>
      
      <div>
        <input
          type="text"
          placeholder="Enter Set 1 elements (comma separated)"
          value={set1Input}
          onChange={(e) => {
            setSet1Input(e.target.value);
            updateSet(e.target.value, 1);
          }}
          style={styles.input}
        />
      </div>

      <div>
        <input
          type="text"
          placeholder="Enter Set 2 elements (comma separated)"
          value={set2Input}
          onChange={(e) => {
            setSet2Input(e.target.value);
            updateSet(e.target.value, 2);
          }}
          style={styles.input}
        />
      </div>

      <div style={styles.setDisplay}>
        <div>Set 1: {`{${set1.join(', ')}}`}</div>
        <div>Set 2: {`{${set2.join(', ')}}`}</div>
      </div>

      <div style={styles.results}>
        <h3>Results:</h3>
        <div>Union: {`{${union.join(', ')}}`}</div>
        <div>Intersection: {`{${intersection.join(', ')}}`}</div>
        <div>Set 1 - Set 2: {`{${difference.join(', ')}}`}</div>
      </div>
    </div>
  );
}