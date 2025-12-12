def task_11(sentence: str) -> None:
    text = sentence.split()
    output = {word: len(word) for word in text if len(word)}
    print(output)
    print(', '.join([word for word, leng in output.items() if leng > 3]))

task_11('I love Python very much')
