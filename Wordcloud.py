import json
import jieba

def main():
    times = {}            # 每个词语出现次数
    dataResults={}        # 最后结果
    results = []
    realWords = []        # 去除停用词后的全部词
    stopWords = [line.strip() for line in open('cn_stopwords.txt', encoding='UTF-8').readlines()]    # 停用词
    txt = open("comment.txt", "r", encoding='utf-8').read()
    allWords = jieba.lcut(txt)
    for i in allWords:
        if i in stopWords:
            continue
        else:
            realWords.append(i)              # 去除停用词

    for i in realWords:
        if len(i) == 1:
            continue
        else:
            times[i] = times.get(i, 0) + 1           # 计算次数

    items = list(times.items())
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语次数依次排序

    for i in range(len(items)):
        result = {}
        word, time = items[i]
        if time > 5:
            result["name"] = word
            result["value"] = time
            results.append(result)          # 结果

    dataResults["data"]=results
    with open("commentTime.json", 'a+', encoding="utf-8") as f:
        json.dump(dataResults, f, ensure_ascii=False, indent=4, )          # 保存

if __name__ == '__main__':
    main()

