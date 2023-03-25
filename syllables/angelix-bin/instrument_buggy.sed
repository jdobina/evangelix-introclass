s/^\s*int\s\+main\s*(.*)/#include <string.h>\n#ifndef ANGELIX_OUTPUT\n#define ANGELIX_OUTPUT(type, expr, id) expr\n#endif\nint main(int argc, char *argv[])/
/printf.*Please enter/d
s/\(^.*\)fgets\s*(\s*\(.*\),\s*\(.*\),\s*stdin\s*);/\1strncpy(\2, argv[1], \3);/
s/\(^.*\)scanf.*,\s*\(.*\)\s*);/\1strcpy(\2, argv[1]);/
s/printf.*The number of syllables.*,\s*\(.\+\)\s*);/printf("%d\\n", ANGELIX_OUTPUT(int, \1, "stdout"));/
s/\r$//
s/\bdouble\b/int/g
s/\bfloat\b/int/g
