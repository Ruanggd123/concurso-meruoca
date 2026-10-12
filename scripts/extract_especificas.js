const fs = require('fs');
const lines = fs.readFileSync('app.js', 'utf8').split('\n');

const qLines = lines.slice(507, 9962);
let qText = qLines.join('\n').trim();
qText = qText.replace(/^const\s+QUIZ_QUESTIONS_DATA\s*=\s*/, '');
if (qText.endsWith(';')) qText = qText.slice(0, -1);

const questions = eval(qText);
console.log('Total questions loaded:', questions.length);

// Filtrar as específicas e de legislação / direito
const especificas = questions.filter(q => 
  ['administrativo', 'legislacao', 'especificos', 'constitucional'].includes(q.category)
);
console.log('Total específicas:', especificas.length);

const discCounter = {};
especificas.forEach(q => discCounter[q.discipline] = (discCounter[q.discipline] || 0) + 1);
console.log('Disciplinas específicas:', discCounter);

fs.writeFileSync('provas/questoes_especificas.json', JSON.stringify(especificas, null, 2), 'utf8');
console.log('Salvo em provas/questoes_especificas.json!');
