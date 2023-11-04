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
	| 'dibagi';
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

DATATYPES: DATA_TYPES;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

atom: BOOLEAN | NUMBER | STRING;

start: program EOF;

program: (variable | callFunction | defineFunction | statement | variableReassignment)*?;

variable: (atom | IDENTIFIER | expression) 'ini' DATATYPES 'nya' IDENTIFIER;

variableReassignment: (atom | IDENTIFIER | expression) 'ini' 'ganti' 'nya' IDENTIFIER;

expression: (atom | IDENTIFIER | callFunction) (
		MATHOPERATORS
		| COMPARISONOPERATORS
	) (atom | IDENTIFIER | callFunction);

callFunction:
	'panggilin' IDENTIFIER 'pake' (
		(atom | IDENTIFIER) ('sama' (atom | IDENTIFIER))*?
	);

defineFunction:
	'ini buat balikin' DATATYPES IDENTIFIER (
		'pake' DATATYPES IDENTIFIER ('sama' DATATYPES IDENTIFIER)*?
	)? '{' program '}';

statement:
	'kalo' expression '{' program '}' (
		'kalo ga' expression '{' program '}'
	)*? ('atoga' '{' program '}')?;
