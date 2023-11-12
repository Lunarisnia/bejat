grammar Bejat;

fragment NEGATIVE_SIGN: '-';
fragment SINGLE_LINE_STRING: '"' (. | ~[\n\r"])*? '"';
fragment DOT: '.';
fragment RAW_NUMBER: NEGATIVE_SIGN? [0-9]+ (DOT [0-9]+)?;
fragment TERNARY: 'bener' | 'salah';
fragment DATA_TYPES: 'nomor' | 'tulisan' | 'bulen';
fragment MATH_OPERATORS:
	'ditambah'
	| 'dikurang'
	| 'dikali'
	| 'dibagi'
	| 'sisa bagi';
fragment COMPARISON_OPERATORS:
	'sama ama'
	| 'ga sama ama'
	| 'lebih dari'
	| 'lebih ato sama ama'
	| 'kurang dari'
	| 'kurang ato sama ama';

WS: [ \t\n\r\f]+ -> skip;
BOOLEAN: TERNARY;
NUMBER: RAW_NUMBER;
STRING: SINGLE_LINE_STRING {self.text = self.text[1:-1]};
MATHOPERATORS: MATH_OPERATORS;
COMPARISONOPERATORS: COMPARISON_OPERATORS;
RETURN: 'balikin';

DATATYPES: DATA_TYPES;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

atom: BOOLEAN | NUMBER | STRING;

start: program EOF;

program: (
		variable
		| callFunction
		| statement
		| variableReassignment
	)*?;

identifier: IDENTIFIER;

variable: (atom | identifier | expression | callFunction) 'ini' DATATYPES 'nya' identifier;

variableReassignment: (
		atom
		| identifier
		| expression
		| callFunction
	) 'ini' 'gantinya' identifier;

expression: (atom | identifier | callFunction) (
		MATHOPERATORS
		| COMPARISONOPERATORS
	) (atom | identifier | callFunction);

callFunction:
	'panggilin' identifier (
		'pake' (atom | identifier | callFunction | expression) ('sama' (atom | identifier | callFunction | expression))*?
	)*?;

// return: RETURN;

// functionBody: program; (return (atom | identifier | expression | callFunction))?;

// defineFunction: 'ini buat balikin' DATATYPES identifier ( 'pake' DATATYPES identifier ('sama'
// DATATYPES identifier)*? )? '{' functionBody '}';

// TODO: should allow return
statement:
	'kalo' expression '{' program '}' (
		'kalo ga' expression '{' program '}'
	)*? ('atoga' '{' program '}')?;