function SetMembershipAnimator() {
  const [elementPositions, setElementPositions] = React.useState([
    { id: 1, text: "A", inSet: false, x: 50, y: 150 },
    { id: 2, text: "B", inSet: false, x: 100, y: 150 }, 
    { id: 3, text: "C", inSet: false, x: 150, y: 150 }
  ]);

  const moveElement = (id) => {
    setElementPositions(positions => 
      positions.map(element => {
        if (element.id === id) {
          return {
            ...element,
            inSet: !element.inSet,
            y: element.inSet ? 150 : 50
          };
        }
        return element;
      })
    );
  };

  return (
    <div style={{ 
      fontFamily: 'Arial',
      padding: '20px'
    }}>
      <h2 style={{ 
        color: '#FF8C00',
        marginBottom: '20px'
      }}>
        Set Membership Animation
      </h2>
      
      <svg width="300" height="200" style={{background: '#FFF5EB'}}>
        {/* Set circle */}
        <circle 
          cx="150" 
          cy="70" 
          r="50" 
          fill="none" 
          stroke="#FFA500" 
          strokeWidth="2"
        />
        
        {/* Set label */}
        <text 
          x="150" 
          y="30" 
          textAnchor="middle" 
          fill="#FF8C00" 
          fontFamily="Arial"
        >
          Set S
        </text>

        {/* Movable elements */}
        {elementPositions.map(element => (
          <g 
            key={element.id}
            onClick={() => moveElement(element.id)}
            style={{cursor: 'pointer'}}
          >
            <circle
              cx={element.x}
              cy={element.y}
              r="15"
              fill="#FFE4B5"
              stroke="#FFA500"
            />
            <text
              x={element.x}
              y={element.y + 5}
              textAnchor="middle"
              fill="#FF8C00"
              fontFamily="Arial"
            >
              {element.text}
            </text>
          </g>
        ))}
      </svg>

      <div style={{
        color: '#FF8C00',
        marginTop: '20px',
        fontSize: '14px'
      }}>
        Click elements to toggle set membership
      </div>
    </div>
  );
}