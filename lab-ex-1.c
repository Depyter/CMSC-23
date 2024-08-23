#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1000

struct word {
    char* string;
};

struct sentence {
    struct word* words;
    int word_count;
};

struct paragraph {
    struct sentence* data;
    int sentence_count;
};

struct document {
    struct paragraph* data;
    int paragraph_count;
};

void initialize_document(char* text, struct document doc) {

    char token[BUFFER_SIZE];

    // Have pointers for each use of strtok recursive
    char* pPtr = NULL;
    char* sPtr = NULL;
    char* wPtr = NULL;

    // Split the text by newline and keep a pointer to reference where it is 
    char* ptoken = strtok_r(text,"\n", &pPtr);

    for (int p = 0; ptoken != NULL; p++) {

        struct paragraph paragaraph;
        paragaraph.sentence_count = 0;
        // Split the paragraph into sentences
        char* stoken = strtok_r(ptoken, ".", &sPtr);

        for (int s = 0; stoken != NULL; s++) {

            struct sentence sentence;
            sentence.words = malloc(sizeof(char));
            sentence.word_count = 0;
            // Split the sentence into words
            char* wtoken = strtok_r(stoken, " ", &wPtr);
            for (int w = 0 ; wtoken != NULL; w++) {

                struct word word;
                // Allocate memory for the string and null terminator
                word.string = malloc(strlen(wtoken) + 1);

                // Have the word.string point to where the wtoken is pointing to
                // So if wtoken changes, the string attribute of the word also changes
                word.string = wtoken;

                sentence.word_count++;
                sentence.words = realloc(sentence.words, sentence.word_count * sizeof(word));

                // Copy the value that word string points to
                // If word.string change, the word in the sentence does not change
                // This is due to how string copying works
                strcpy(sentence.words[s].string, word.string);
                wtoken = strtok_r(NULL, " ", &wPtr);
            }
            stoken = strtok_r(NULL, ".", &sPtr);
        }

        ptoken = strtok_r(NULL, "\n", &pPtr);
    }
}

int main() {
    int number;
    scanf("%d", &number);
    // Leaves a trailing newline
    char text[BUFFER_SIZE];

    // Consume the trailing newline
    getchar();

    for (int i = 0; i < number; i++) {

        // Store newline then concatenate it to the text string
        char newLine[BUFFER_SIZE];
        fgets(newLine, BUFFER_SIZE, stdin);

        // Remove the trailing newline of the last line
        if ((i + 1) == number)
            newLine[strcspn(newLine, "\n")] = 0;
        strcat(text,newLine);
    }

    struct document doc;
    initialize_document(text, doc);

    return 0;
}
