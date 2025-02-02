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