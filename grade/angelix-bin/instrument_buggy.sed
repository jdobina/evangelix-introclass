/int$/N
s/^\s*int\s\+main\s*(.*)/#include <stdlib.h>\n#ifndef ANGELIX_OUTPUT\n#define ANGELIX_OUTPUT(type, expr, id) expr\n#endif\nint main(int argc, char *argv[])/
/printf.*Enter thresholds/d
/printf.*Thank you/d
s/\(^.*\)scanf.*,\s*&\(.*\),\s*&\(.*\),\s*&\(.*\),\s*&\(.*\)\s*);/\1\2 = atoi(argv[1]);\n\1\3 = atoi(argv[2]);\n\1\4 = atoi(argv[3]);\n\1\5 = atoi(argv[4]);/
s/\(^.*\)scanf.*,\s*&\(.*\)\s*);/\1\2 = atoi(argv[5]);/
s/printf.*Student has.*grade.*,\s*\(.\+\)\s*);/printf("%c\\n", ANGELIX_OUTPUT(char, \1, "stdout"));/
s/\r$//
s/\bdouble\b/int/g
s/\bfloat\b/int/g
