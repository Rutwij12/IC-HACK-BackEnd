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