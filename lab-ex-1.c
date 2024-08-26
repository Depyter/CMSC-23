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
    struct sentence* sentences;
    int sentence_count;
};

struct document {
    struct paragraph* paragraphs;
    int paragraph_count;
};

// Function to free memory allocated for a document
void free_document(struct document* doc) {
    for (int i = 0; i < doc->paragraph_count; i++) {
        struct paragraph* para = &doc->paragraphs[i];
        for (int j = 0; j < para->sentence_count; j++) {
            struct sentence* sent = &para->sentences[j];
            for (int k = 0; k < sent->word_count; k++) {
                free(sent->words[k].string);
            }
            free(sent->words);
        }
        free(para->sentences);
    }
    free(doc->paragraphs);
}

// Function to print a sentence
void print_sentence(struct sentence* sent) {
    for (int i = 0; i < sent->word_count; i++) {
        printf("%s", sent->words[i].string);
        if (i < sent->word_count - 1) {
            printf(" ");
        }
    }
    printf(".");
}

// Function to print all sentences in a paragraph
void print_paragraph(struct paragraph* para) {
    for (int i = 0; i < para->sentence_count; i++) {
        print_sentence(&para->sentences[i]);
    }
    printf("\n");
}

void initialize_document(char* text, struct document* doc, int number) {

    // Have pointers for each use of strtok_r
    char* pPtr = NULL;
    char* sPtr = NULL;
    char* wPtr = NULL;

    // Allocating memory to store pointers in an array to struct paragraphs 
    doc->paragraphs = malloc(number * sizeof(struct paragraph));
    doc->paragraph_count = 0;

    // Split the text by newline and keep a pointer to reference where it is 
    char* ptoken = strtok_r(text, "\n", &pPtr);

    for (int p = 0; ptoken != NULL; p++) {

        struct paragraph paragaraph;
        paragaraph.sentence_count = 0;
        
        // Allocating memory to store pointers in an array to struct sentences
        paragaraph.sentences = malloc(5 * sizeof(struct sentence));

        // Split the paragraph into sentences
        char* stoken = strtok_r(ptoken, ".", &sPtr);

        for (int s = 0; stoken != NULL; s++) {

            struct sentence sentence;
            sentence.words = malloc(1000 * sizeof(struct word));
            sentence.word_count = 0;

            // Split the sentence into words
            char* wtoken = strtok_r(stoken, " ", &wPtr);

            for (int w = 0; wtoken != NULL; w++) {

                // Allocate memory for the word and copy it to the struct
                struct word word;
                word.string = malloc(strlen(wtoken) + 1);
                strcpy(word.string, wtoken);

                // For each word, put it in a pointer (struct* words) array for that sentence
                sentence.words[sentence.word_count] = word;
                sentence.word_count++;

                wtoken = strtok_r(NULL, " ", &wPtr);
            }

            // Put that sentence, into another pointer (struct* sentences) for that paragraph
            paragaraph.sentences[paragaraph.sentence_count] = sentence;
            paragaraph.sentence_count++;

            stoken = strtok_r(NULL, ".", &sPtr);
        }

        // Put that paragraph, into another pointer (struct* paragraphs) for the document
        doc->paragraphs[doc->paragraph_count] = paragaraph;
        doc->paragraph_count++;
        ptoken = strtok_r(NULL, "\n", &pPtr);

        // Essentially, the "higher" struct merely store the pointer
        // struct word stores the pointer to the char array
        // struct sentence stores an array of pointers to struct words
        // struct paragraph stores an array of pointers to sentences
        // struct doc stores an array of pointers to paragraphs
    }
}

// Function to validate the index and print error if invalid
void validate_index(int index, int max, const char* type) {
    if (index >= max) {
        printf("Invalid %s index.\n", type);
        exit(1);
    }
}

struct word* kth_word_in_mth_sentence_in_nth_paragraph(int k, int m, int n, struct document* doc) {
    validate_index(n, doc->paragraph_count, "paragraph");

    struct paragraph* paragraph = &doc->paragraphs[n];
    validate_index(m, paragraph->sentence_count, "sentence");

    struct sentence* sentence = &paragraph->sentences[m];
    validate_index(k, sentence->word_count, "word");

    return &sentence->words[k];
}

struct sentence* kth_sentence_in_mth_paragraph(int k, int m, struct document* doc) {
    validate_index(m, doc->paragraph_count, "paragraph");

    struct paragraph* paragraph = &doc->paragraphs[m];
    validate_index(k, paragraph->sentence_count, "sentence");

    return &paragraph->sentences[k];
}

struct paragraph* kth_paragraph(int k, struct document* doc) {
    validate_index(k, doc->paragraph_count, "paragraph");

    return &doc->paragraphs[k];
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
    initialize_document(text, &doc, number);
    
    int q;
    scanf("%d", &q);
    getchar();
    for (int z = 0; z < q; z++) {
        int k, m, n, f;
        int numArgs;
        char input[100];
        fgets(input, sizeof(input), stdin);

        // Match input and store the number of matched inputs
        numArgs = sscanf(input, "%d %d %d %d", &f, &k, &m, &n);
    
        // Use switch-case to call the appropriate function
        switch (numArgs - 1) {
            case 1:
                // Only k was provided
                print_paragraph(kth_paragraph(k - 1, &doc));
                break;
            case 2:
                // k and m were provided
                print_sentence(kth_sentence_in_mth_paragraph(k - 1, m - 1, &doc));
                printf("\n");
                break;
            case 3:
                // k, m, and n were provided
                printf("%s\n", kth_word_in_mth_sentence_in_nth_paragraph(k -1, m - 1, n - 1, &doc)->string);
                break;
            default:
                printf("Invalid input format.\n");
                break;
        }
    }
    free_document(&doc);
    return 0;
}
