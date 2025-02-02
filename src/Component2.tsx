function VennDiagramInteractive() {
  const [selectedOperation, setSelectedOperation] = React.useState('intersection');
  const [draggedElement, setDraggedElement] = React.useState(null);
  const [elements, setElements] = React.useState({
    setA: [{id: 1, x: 100, y: 150}, {id: 2, x: 150, y: 150}],
    setB: [{id: 3, x: 250, y: 150}, {id: 4, x: 300, y: 150}]
  });

  const handleDragStart = (e, elementId, set) => {
    setDraggedElement({ id: elementId, set });
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e, targetSet) => {
    e.preventDefault();
    if (!draggedElement) return;

    const { id, set: sourceSet } = draggedElement;
    if (sourceSet === targetSet) return;

    // Move element between sets
    setElements(prev => {
      const newElements = { ...prev };
      const elementToMove = prev[sourceSet].find(el => el.id === id);
      newElements[sourceSet] = prev[sourceSet].filter(el => el.id !== id);
      newElements[targetSet] = [...prev[targetSet], elementToMove];
      return newElements;
    });
  };

  const getResultSet = () => {
    switch (selectedOperation) {
      case 'union':
        return [...elements.setA, ...elements.setB];
      case 'intersection':
        return elements.setA.filter(a => 
          elements.setB.some(b => Math.abs(a.x - b.x) < 50 && Math.abs(a.y - b.y) < 50)
        );
      default:
        return [];
    }
  };

  return (
    <div style={{ fontFamily: 'Arial', color: '#FF8C00' }}>
      <h2 style={{ fontSize: '24px', color: '#FF4500' }}>Interactive Venn Diagram</h2>
      
      <div style={{ marginBottom: '20px' }}>
        <select 
          value={selectedOperation}
          onChange={(e) => setSelectedOperation(e.target.value)}
          style={{ padding: '5px', margin: '10px' }}
        >
          <option value="intersection">Intersection</option>
          <option value="union">Union</option>
        </select>
      </div>

      <div style={{ position: 'relative', width: '600px', height: '300px', border: '1px solid #FFA500' }}>
        {/* Set A Circle */}
        <div
          onDragOver={handleDragOver}
          onDrop={(e) => handleDrop(e, 'setA')}
          style={{
            position: 'absolute',
            left: '100px',
            top: '50px',
            width: '200px',
            height: '200px',
            borderRadius: '50%',
            border: '2px solid #FFA500',
            opacity: 0.5
          }}
        >
          {elements.setA.map(element => (
            <div
              key={element.id}
              draggable
              onDragStart={(e) => handleDragStart(e, element.id, 'setA')}
              style={{
                position: 'absolute',
                left: element.x - 100,
                top: element.y - 50,
                width: '20px',
                height: '20px',
                background: '#FF8C00',
                borderRadius: '50%',
                cursor: 'move'
              }}
            />
          ))}
        </div>

        {/* Set B Circle */}
        <div
          onDragOver={handleDragOver}
          onDrop={(e) => handleDrop(e, 'setB')}
          style={{
            position: 'absolute',
            left: '200px',
            top: '50px',
            width: '200px',
            height: '200px',
            borderRadius: '50%',
            border: '2px solid #FFA500',
            opacity: 0.5
          }}
        >
          {elements.setB.map(element => (
            <div
              key={element.id}
              draggable
              onDragStart={(e) => handleDragStart(e, element.id, 'setB')}
              style={{
                position: 'absolute',
                left: element.x - 200,
                top: element.y - 50,
                width: '20px',
                height: '20px',
                background: '#FF8C00',
                borderRadius: '50%',
                cursor: 'move'
              }}
            />
          ))}
        </div>
      </div>

      <div style={{ marginTop: '20px' }}>
        <h3 style={{ fontSize: '18px', color: '#FF7F50' }}>Result Set</h3>
        <p>Number of elements: {getResultSet().length}</p>
      </div>
    </div>
  );
}