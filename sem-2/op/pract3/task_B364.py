# Дан список строк, состоящий из названий файлов с расширением.
# Написать функцию extension, которая возвращает список расширений наибольшего количества файлов
#
# Пример:
# extension(["Lakey - Better days.mp3", "Wheathan - Superlove.wav", "groovy jam.als",
#  "#4 final mixdown.als", "album cover.ps", "good nights.mp3" ]) ==> [".als", ".mp3"]
import traceback
import os

def extension(files):
    l = []
    # Создаем пустой список l
    for i in files:
        # Цикл for, проходящий по каждому элементу в списке files
        l.append(os.path.splitext(i)[1])
        # Извлекаем расширение файла i с помощью функции os.path.splitext и добавляем его в список l
    ot = [item for item in set(l) if l.count(item) >= max(map(lambda x: l.count(x), l))]
    # Создаем новый список ot, содержащий уникальные элементы из списка l, для которых количество их вхождений в l
    # больше или равно максимальному количеству вхождений элементов в l
    ot.sort()
    # Сортируем список ot в порядке возрастания
    return ot
    # Возвращаем отсортированный список ot, содержащий наиболее распространенные расширения файлов в списке files



# Тесты
try:
    assert extension(["direful.pr", "festive.html", "historical.wav", "holistic.mp3", "impossible.jar",
                      "gentle.cpp", "gleaming.xml", "inconclusive.js", "rect.jar", "befitting.mp3",
                      "brief.wp", "beautiful.jar", "energetic.pt", "careful.wp", "defective.cpp", "icky.wav",
                      "gorgeous.txt", "good.pt", "fat.pt", "bored.als", "adaptable.cpp", "fumbling.exe",
                      "grieving.wp", "efficient.wav", "fearful.xml", "damp.html", "erect.exe", "annoyed.xml",
                      "elderly.ala", "far-flung.txt", "careful.mp3", "actually.pt", "cynical.ala", "complex.exe",
                      "extra-small.pt", "enchanted.ala", "amazing.html", "bashful.h", "hallowed.html",
                      "entertaining.html", "bad.js", "illegal.maya", "deadpan.html", "furtive.wp", "hanging.css",
                      "drunk.py", "capricious.wav", "damaging.Ue4", "cool.Ue4", "ambitious.css", "fortunate.wp",
                      "electric.mp3", "crowded.txt", "cooperative.html", "graceful.pt", "aboard.pt", "exclusive.als",
                      "glossy.css", "fluffy.pt", "cluttered.txt", "halting.cpp", "glib.cpp", "aback.pr",
                      "cynical.Ue4", "chilly.xml", "hideous.ala", "finicky.txt", "feigned.ala", "better.Ue4",
                      "dear.py", "available.xml", "easy.pr", "fine.mp3", "cowardly.jar", "incredible.css",
                      "adhesive.exe", "energetic.mp3", "harmonious.exe", "general.als", "condemned.als",
                      "flawless.als", "curvy.h", "ambitious.mp3", "disillusioned.xml", "bitter.h",
                      "hanging.wp", "certain.cpp", "flashy.html", "cuddly.pr", "cagey.Ue4", "extra-small.pr",
                      "amuck.cpp", "direful.html", "delightful.als", "helpless.h", "foamy.mp3", "enthusiastic.maya",
                      "good.maya", "adhesive.css", "imperfect.pr", "bent.cpp", "exultant.zbrush", "adorable.mp3",
                      "clammy.maya", "gaudy.pt", "blushing.css", "cuddly.Ue4", "curved.py", "boring.html", "broken.txt",
                      "daily.jar", "giddy.xml", "curved.css", "future.maya", "graceful.css", "guiltless.maya",
                      "gentle.cpp", "few.css", "calculating.txt", "clear.pr", "grey.py", "entertaining.ala",
                      "elfin.txt", "excited.js", "abject.zbrush", "best.js", "boundless.wav", "hurried.ala",
                      "delirious.cpp"]) == [".cpp", ".html"]
    assert extension(["dramatic.txt", "incompetent.jar", "alcoholic.wp", "clumsy.py", "abject.h", "boring.exe",
                      "aloof.pr", "familiar.py", "fanatical.py", "ill-informed.html", "fierce.pr", "accurate.html",
                      "grotesque.pr", "brown.py", "courageous.pt", "grouchy.jar", "giant.pt", "dirty.h",
                      "abaft.jar", "enormous.zbrush", "creepy.cpp", "beneficial.py", "absorbing.ala",
                      "heartbreaking.html", "exclusive.js", "fluttering.html", "happy.als", "fresh.pr",
                      "adamant.txt", "awful.maya", "frightening.maya", "bizarre.html", "efficacious.exe",
                      "illegal.wav", "dizzy.js", "gusty.wp", "delightful.pt", "full.als", "chivalrous.xml",
                      "filthy.js", "functional.jar", "conscious.wav", "feeble.exe", "hilarious.cpp", "earthy.py",
                      "handy.txt", "hollow.cpp", "aggressive.js", "fat.h", "drunk.exe", "clear.h", "easy.wav",
                      "eatable.pt", "grumpy.css", "empty.exe", "brief.jar", "aggressive.txt", "aggressive.txt",
                      "gruesome.ala", "awake.txt", "apathetic.mp3", "holistic.pt", "embarrassed.css", "flashy.maya",
                      "exultant.ala", "exuberant.exe", "graceful.pt", "dependent.py", "gigantic.wp", "husky.js",
                      "immense.pr", "defiant.cpp", "cooperative.html", "frantic.maya", "abashed.css",
                      "dysfunctional.h", "gusty.js", "dynamic.txt", "dreary.pt", "giddy.ala", "exciting.css",
                      "best.als", "humdrum.css", "busy.jar", "frail.cpp", "cagey.wav"]) == [".pt", ".py", ".txt"]
    assert extension(["crazy.pr", "black-and-white.als", "illegal.wav", "exultant.mp3", "exotic.jar", "capricious.pt",
                      "abundant.ala", "eatable.zbrush", "careful.py", "godly.css", "clever.txt", "dusty.maya",
                      "awesome.zbrush", "discreet.jar", "creepy.h", "fair.pt", "descriptive.mp3", "boundless.ala",
                      "berserk.xml", "hungry.exe", "awful.exe"]) == [".ala", ".exe", ".jar", ".mp3", ".pt", ".zbrush"]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
