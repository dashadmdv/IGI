from src.functions import count_sentences, count_non_declarative, calc_average_sentence_length, \
    calc_average_word_length, calculate_top_k_repeated_n_grams


def main():
    try:
        text = input("Input text to analyze\n")
        print("Amount of sentences: " + str(count_sentences(text)))
        print("Amount of non-declarative sentences: " + str(count_non_declarative(text)))

        try:
            print(f'Average sentence length: {calc_average_sentence_length(text)} characters')
            print("Average word length: " + str(calc_average_word_length(text)))

        except ZeroDivisionError:
            print("No sentence has been inputted!")

        try:
            n, k = map(int, input("Enter N and K to get top K repeated N-grams in the text: ").split())
            ngrams = calculate_top_k_repeated_n_grams(text, k, n)
            if len(ngrams) == 0:
                print(f'No such {n}grams!')
            else:
                print(f'Top {k} repeated {n}-grams: \n {ngrams}')

        except ValueError:
            ngrams = calculate_top_k_repeated_n_grams(text)
            if len(ngrams) == 0:
                print(f'No such {4} grams!')
            else:
                print(f'Top 10 repeated 4-grams: \n {ngrams}')

    except KeyboardInterrupt:
        print("See you later!")


if __name__ == '__main__':
    main()
