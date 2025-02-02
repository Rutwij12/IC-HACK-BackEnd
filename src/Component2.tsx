function VennDiagramVisualizer() {
  const [sets, setSets] = React.useState({
    setA: {x: 150, y: 150, elements: ['A1', 'A2', 'A3']},
    setB: {x: 250, y: 150, elements: ['B1', 'B2', 'A2']} 
  });
  const [draggedSet, setDraggedSet] = React.useState(null);
  const [mouseOffset, setMouseOffset] = React.useState({x: 0, y: 0});

  const handleMouseDown = (e, setKey) => {
    const rect = e.target.getBoundingClientRect();
    setMouseOffset({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
    });
    setDraggedSet(setKey);
  };

  const handleMouseMove = (e) => {
    if (draggedSet) {
      setSets(prev => ({
        ...prev,
        [draggedSet]: {
          ...prev[draggedSet],
          x: e.clientX - mouseOffset.x,
          y: e.clientY - mouseOffset.y
        }
      }));
    }
  };

  const handleMouseUp = () => {
    setDraggedSet(null);
  };

  const getIntersection = () => {
    return sets.setA.elements.filter(el => sets.setB.elements.includes(el));
  };

  const getUnion = () => {
    return [...new Set([...sets.setA.elements, ...sets.setB.elements])];
  };

  return (
    <div 
      style={{
        position: 'relative',
        height: '400px',
        fontFamily: 'Arial',
        userSelect: 'none'
      }}
      onMouseMove={handleMouseMove}
      onMouseUp={handleMouseUp}
    >
      <h2 style={{color: '#FF8C00', marginBottom: '20px'}}>Interactive Venn Diagram</h2>
      
      {/* Set A Circle */}
      <div
        style={{
          position: 'absolute',
          left: sets.setA.x,
          top: sets.setA.y,
          width: '150px',
          height: '150px',
          borderRadius: '50%',
          backgroundColor: 'rgba(255, 140, 0, 0.3)',
          cursor: 'move',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}
        onMouseDown={(e) => handleMouseDown(e, 'setA')}
      >
        Set A
      </div>

      {/* Set B Circle */}
      <div
        style={{
          position: 'absolute',
          left: sets.setB.x,
          top: sets.setB.y,
          width: '150px',
          height: '150px',
          borderRadius: '50%',
          backgroundColor: 'rgba(255, 160, 0, 0.3)',
          cursor: 'move',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}
        onMouseDown={(e) => handleMouseDown(e, 'setB')}
      >
        Set B
      </div>

      {/* Operations Display */}
      <div style={{
        position: 'absolute',
        top: '320px',
        left: '20px',
        color: '#FF8C00'
      }}>
        <p>Intersection: {getIntersection().join(', ')}</p>
        <p>Union: {getUnion().join(', ')}</p>
      </div>
    </div>
  );
}