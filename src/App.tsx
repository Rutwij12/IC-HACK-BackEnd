import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';

function SetDefinitionCard() {
  return (
    <div style={{
      fontFamily: 'Arial',
      padding: '20px',
      maxWidth: '600px',
      borderRadius: '8px',
      backgroundColor: '#fff6eb'  
    }}>
      <h2 style={{
        fontSize: '24px',
        color: '#e65c00',
        marginBottom: '15px'
      }}>
        What is a Mathematical Set?
      </h2>
      
      <p style={{
        fontSize: '16px',
        color: '#cc5200',
        lineHeight: '1.6',
        marginBottom: '15px'
      }}>
        A set is a collection of distinct objects, considered as a single unit. The objects in a set are called elements or members of the set. Sets are usually denoted by capital letters.
      </p>

      <div style={{
        fontSize: '16px',
        color: '#e67300',
        marginBottom: '15px'
      }}>
        <h3 style={{
          fontSize: '18px',
          color: '#cc5200',
          marginBottom: '10px'
        }}>
          Simple Examples:
        </h3>
        <ul style={{lineHeight: '1.6'}}>
          <li>A = {'{'}1, 2, 3, 4, 5{'}'} is a set of first five natural numbers</li>
          <li>B = {'{'}red, blue, green{'}'} is a set of colors</li>
          <li>C = {'{'}dog, cat, rabbit{'}'} is a set of animals</li>
        </ul>
      </div>

      <p style={{
        fontSize: '16px',
        color: '#cc5200',
        fontStyle: 'italic'
      }}>
        Key characteristic: Each element in a set must be unique, and the order of elements doesn't matter.
      </p>
    </div>
  );
}
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
function SetNotationGuide() {
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
    section: {
      marginBottom: '24px'
    },
    sectionTitle: {
      fontSize: '20px',
      color: '#e67300',
      marginBottom: '12px'
    },
    text: {
      fontSize: '16px',
      lineHeight: '1.6',
      marginBottom: '12px'
    },
    example: {
      fontStyle: 'italic',
      color: '#ff9933',
      marginLeft: '20px'
    }
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Set Notation Guide</h1>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Definition</h2>
        <p style={styles.text}>
          A set is denoted by curly braces {} containing its elements, separated by commas.
        </p>
        <p style={styles.example}>Example: {"{1, 2, 3}"} is a set containing three numbers</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Membership</h2>
        <p style={styles.text}>
          The symbol ∈ means "is an element of" and ∉ means "is not an element of"
        </p>
        <p style={styles.example}>Example: x ∈ A means x is an element of set A</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Common Sets</h2>
        <p style={styles.text}>
          ℕ represents Natural Numbers
          ℤ represents Integers
          ℚ represents Rational Numbers
          ℝ represents Real Numbers
        </p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Operations</h2>
        <p style={styles.text}>
          ∪ represents Union: combines elements from both sets
          ∩ represents Intersection: elements common to both sets
          \ represents Set Difference: elements in first set but not in second
        </p>
        <p style={styles.example}>Example: A ∪ B contains all elements from both A and B</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Set Properties</h2>
        <p style={styles.text}>
          ⊆ means "is a subset of"
          ⊂ means "is a proper subset of"
          = means sets contain exactly the same elements
        </p>
        <p style={styles.example}>Example: If A ⊆ B, all elements of A are also in B</p>
      </div>

      <div style={styles.section}>
        <h2 style={styles.sectionTitle}>Special Sets</h2>
        <p style={styles.text}>
          ∅ or {} represents the Empty Set
          U represents the Universal Set
        </p>
        <p style={styles.example}>Example: The empty set ∅ contains no elements</p>
      </div>
    </div>
  )
}
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
function CommonSetsExplainer() {
  return (
    <div style={{ fontFamily: 'Arial', color: '#FF8C42', padding: '20px' }}>
      <h2 style={{ 
        fontSize: '28px', 
        color: '#E85D04', 
        marginBottom: '20px' 
      }}>
        Common Sets in Everyday Life
      </h2>

      <div style={{ marginBottom: '15px' }}>
        <h3 style={{ 
          fontSize: '20px',
          color: '#F48C06',
          marginBottom: '10px'
        }}>
          In the Kitchen
        </h3>
        <p style={{ fontSize: '16px', lineHeight: '1.6' }}>
          Your kitchen utensils form a set: {'{spoons, forks, knives, spatulas}'}.
          The ingredients in your fridge are another set.
        </p>
      </div>

      <div style={{ marginBottom: '15px' }}>
        <h3 style={{
          fontSize: '20px',
          color: '#F48C06',
          marginBottom: '10px'
        }}>
          At School
        </h3>
        <p style={{ fontSize: '16px', lineHeight: '1.6' }}>
          A classroom contains the set of students, the set of desks, and the set of school supplies.
        </p>
      </div>

      <div style={{ marginBottom: '15px' }}>
        <h3 style={{
          fontSize: '20px',
          color: '#F48C06',
          marginBottom: '10px'
        }}>
          In Nature
        </h3>
        <p style={{ fontSize: '16px', lineHeight: '1.6' }}>
          Trees in a forest form a set. Animals in a zoo form a set.
          Even the planets in our solar system form a set: {'{Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune}'}.
        </p>
      </div>

      <div style={{ marginBottom: '15px' }}>
        <h3 style={{
          fontSize: '20px',
          color: '#F48C06',
          marginBottom: '10px'
        }}>
          In Your Closet
        </h3>
        <p style={{ fontSize: '16px', lineHeight: '1.6' }}>
          Your clothes form different sets: the set of shirts, the set of pants, the set of shoes.
          These are all subsets of your complete wardrobe set.
        </p>
      </div>
    </div>
  );
}
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

function App() {
  return (
    <div>
      <SetDefinitionCard />
      <div style={{ marginBottom: '2rem' }} />
      <VennDiagramVisualizer />
      <div style={{ marginBottom: '2rem' }} />
      <SetNotationGuide />
      <div style={{ marginBottom: '2rem' }} />
      <SetMembershipAnimator />
      <div style={{ marginBottom: '2rem' }} />
      <CommonSetsExplainer />
      <div style={{ marginBottom: '2rem' }} />
      <SetOperationsCalculator />
      <div style={{ marginBottom: '2rem' }} />
    </div>
  );
}

export default App;