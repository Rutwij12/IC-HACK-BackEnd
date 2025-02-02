const ResultPreview = ({ before, after, label }) => {
  const [isShowingAfter, setIsShowingAfter] = useState(false);
  
  const containerStyle = {
    fontFamily: 'Arial',
    padding: '20px',
    border: '2px solid #2196F3',
    borderRadius: '8px',
    maxWidth: '300px',
    color: '#0D47A1'
  };

  const headerStyle = {
    fontSize: '18px',
    marginBottom: '15px',
    color: '#1565C0'
  };

  const resultStyle = {
    fontSize: '16px',
    padding: '10px',
    backgroundColor: '#E3F2FD',
    borderRadius: '4px',
    marginBottom: '10px'
  };

  const buttonStyle = {
    backgroundColor: '#2196F3',
    color: 'white',
    border: 'none',
    padding: '8px 16px',
    borderRadius: '4px',
    cursor: 'pointer',
    fontFamily: 'Arial',
    fontSize: '14px'
  };

  const toggleView = () => {
    setIsShowingAfter(!isShowingAfter);
  };

  return (
    <div style={containerStyle}>
      <div style={headerStyle}>{label || 'Transform Preview'}</div>
      
      <div style={resultStyle}>
        {isShowingAfter ? (
          <span>After: {after}</span>
        ) : (
          <span>Before: {before}</span>
        )}
      </div>

      <button 
        style={buttonStyle}
        onClick={toggleView}
      >
        Show {isShowingAfter ? 'Before' : 'After'}
      </button>
    </div>
  );
};