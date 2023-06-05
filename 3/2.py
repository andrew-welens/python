answers, student_answers = [
    "Dryopithecus",
    "Ramapithecus",
    "Australopithecus",
    "Homo Erectus",
    "Homo Sapiens Neanderthalensis",
    "Homo Sapiens Sapiens"
], []
hasErrors = 0

for i in range(len(answers)):
    student_answers.append(input(f'Вопрос: {i + 1} этап развития человека?: '))
    if answers[i].lower() != student_answers[i].lower():
        hasErrors = hasErrors + 1

print(f'Результат тестирования\nПравильные: {len(answers) - hasErrors}\t Ошибки: {hasErrors}\nПравильный ответ:\n');
print(' => '.join(answers))
