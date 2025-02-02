function SetMembershipVisualizer() {
  const [elements, setElements] = React.useState([
    { id: 1, value: 'A', inSet: true },
    { id: 2, value: 'B', inSet: false },
    { id: 3, value: 'C', inSet: true },
    { id: 4, value: 'D', inSet: false }
  ]);

  const toggleMembership = (id) => {
    setElements(elements.map(element => 
      element.id === id ? { ...element, inSet: !element.inSet } : element
    ));
  };

  const styles = {
    container: {
      fontFamily: 'Arial',
      padding: '20px',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center'
    },
    title: {
      fontSize: '24px',
      color: '#ff8c00',
      marginBottom: '20px'
    },
    setContainer: {
      border: '3px solid #ffa500',
      borderRadius: '50%',
      width: '300px',
      height: '300px',
      position: 'relative',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center'
    },
    element: {
      cursor: 'pointer',
      padding: '10px',
      margin: '5px',
      borderRadius: '50%',
      width: '30px',
      height: '30px',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      position: 'absolute',
      transition: 'all 0.5s ease',
      backgroundColor: '#fff',
      border: '2px solid #ff8c00',
      color: '#ff8c00',
      fontWeight: 'bold'
    },
    legend: {
      marginTop: '20px',
      color: '#ff8c00',
      fontSize: '16px'
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Set Membership Visualizer</h2>
      
      <div style={styles.setContainer}>
        {elements.map((element, index) => {
          const angle = (index * 360) / elements.length;
          const radius = element.inSet ? 70 : 130;
          const left = 150 + radius * Math.cos((angle * Math.PI) / 180);
          const top = 150 + radius * Math.sin((angle * Math.PI) / 180);
          
          return (
            <div
              key={element.id}
              style={{
                ...styles.element,
                left: `${left}px`,
                top: `${top}px`,
                backgroundColor: element.inSet ? '#fff3e0' : '#fff'
              }}
              onClick={() => toggleMembership(element.id)}
            >
              {element.value}
            </div>
          );
        })}
      </div>
      
      <div style={styles.legend}>
        Click elements to toggle set membership
      </div>
    </div>
  );
}