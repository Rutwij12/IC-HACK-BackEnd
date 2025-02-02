import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function SetDefinitionText() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#cc7000'
    },
    title: {
      fontSize: '28px',
      color: '#ff8c00',
      marginBottom: '20px'
    },
    subtitle: {
      fontSize: '22px',
      color: '#ffa500',
      marginTop: '20px',
      marginBottom: '12px'
    },
    text: {
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '16px'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Understanding Mathematical Sets</h1>

      <h2 style={styles.subtitle}>What is a Set?</h2>
      <p style={styles.text}>
        A set is a collection of distinct objects, considered as an object in its own right. The objects in a set are called its elements or members. Sets are usually denoted by capital letters.
      </p>

      <h2 style={styles.subtitle}>Basic Properties of Sets</h2>
      <p style={styles.text}>
        Sets have several fundamental properties:
        • Sets are unordered - the order of elements doesn't matter
        • Sets contain unique elements - no duplicates are allowed
        • Sets can be finite or infinite in size
        • Sets can contain any type of objects
      </p>

      <h2 style={styles.subtitle}>Set Notation</h2>
      <p style={styles.text}>
        Sets are typically written using curly braces. The elements inside can be listed explicitly or described using a rule or condition. A set can also be empty, containing no elements at all.
      </p>

      <h2 style={styles.subtitle}>Working with Sets</h2>
      <p style={styles.text}>
        Sets can be manipulated through various operations like union (combining sets), intersection (finding common elements), and complement (elements not in a set). These operations allow us to solve complex problems and represent relationships between different groups of objects.
      </p>
    </div>
  )
}
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
function SetNotationGuide() {
  const titleStyle = {
    fontFamily: 'Arial',
    fontSize: '28px',
    color: '#FF8C00',
    marginBottom: '20px'
  }

  const sectionTitleStyle = {
    fontFamily: 'Arial', 
    fontSize: '20px',
    color: '#FFA500',
    marginTop: '15px',
    marginBottom: '10px'
  }

  const textStyle = {
    fontFamily: 'Arial',
    fontSize: '16px',
    color: '#FF7F50',
    lineHeight: '1.6',
    marginBottom: '10px'
  }

  return (
    <div style={{padding: '20px'}}>
      <h1 style={titleStyle}>Set Notation Guide</h1>

      <h2 style={sectionTitleStyle}>Basic Set Notation</h2>
      <p style={textStyle}>
        • Set Definition: {'{}'} represents an empty set<br/>
        • Element Membership: ∈ means "is an element of"<br/>
        • Not an Element: ∉ means "is not an element of"<br/>
        • Example: x ∈ {'{1, 2, 3}'} means x is in the set {'{1, 2, 3}'}
      </p>

      <h2 style={sectionTitleStyle}>Set Operations</h2>
      <p style={textStyle}>
        • Union: ∪ combines elements from both sets<br/>
        • Intersection: ∩ keeps elements common to both sets<br/>
        • Subset: ⊆ means "is a subset of"<br/>
        • Proper Subset: ⊂ means "is a proper subset of"
      </p>

      <h2 style={sectionTitleStyle}>Set Construction</h2>
      <p style={textStyle}>
        • List Notation: {'{a, b, c}'}<br/>
        • Set Builder: {'{ x | P(x) }'} means "the set of all x such that P(x)"<br/>
        • Intervals: [a,b] represents closed interval, (a,b) represents open interval
      </p>

      <h2 style={sectionTitleStyle}>Common Sets</h2>
      <p style={textStyle}>
        • ℕ - Natural numbers<br/>
        • ℤ - Integers<br/>
        • ℚ - Rational numbers<br/>
        • ℝ - Real numbers<br/>
        • ∅ - Empty set
      </p>

      <h2 style={sectionTitleStyle}>Cardinality</h2>
      <p style={textStyle}>
        • |A| represents the number of elements in set A<br/>
        • Example: |{'{1, 2, 3}'}| = 3<br/>
        • Empty set has cardinality 0: |∅| = 0
      </p>
    </div>
  )
}
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
function SetOperationsExplainer() {
  const styles = {
    container: {
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '20px auto',
      padding: '20px',
      color: '#CC7000'
    },
    title: {
      fontSize: '28px',
      color: '#FF8C00',
      marginBottom: '20px'
    },
    section: {
      marginBottom: '24px'
    },
    sectionTitle: {
      fontSize: '20px',
      color: '#FFA500',
      marginBottom: '12px'
    },
    content: {
      fontSize: '16px',
      lineHeight: '1.6',
      color: '#E67300'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Set Operations Explained</h1>
      
      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Union</h2>
        <p style={styles.content}>
          The union of two sets A and B is the set that contains all elements from both A and B, with duplicates removed. 
          It represents combining all unique elements from both sets into a single set. The union is denoted as A ∪ B.
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Intersection</h2>
        <p style={styles.content}>
          The intersection of two sets A and B is the set containing only the elements that appear in both A and B.
          It represents the common elements between two sets. The intersection is denoted as A ∩ B.
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Complement</h2>
        <p style={styles.content}>
          The complement of a set A is all elements in the universal set that are not in A.
          It represents everything that is not included in the original set. The complement is denoted as A' or A^c.
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Difference</h2>
        <p style={styles.content}>
          The difference between sets A and B (A - B) is the set of elements that are in A but not in B.
          It represents what remains in the first set after removing elements that appear in the second set.
        </p>
      </div>
    </div>
  )
}

function App() {
  return (
    <div>
      <SetDefinitionText />
      <div style={{ marginBottom: '2rem' }} />
      <VennDiagramInteractive />
      <div style={{ marginBottom: '2rem' }} />
      <SetNotationGuide />
      <div style={{ marginBottom: '2rem' }} />
      <SetMembershipVisualizer />
      <div style={{ marginBottom: '2rem' }} />
      <SetOperationsExplainer />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;