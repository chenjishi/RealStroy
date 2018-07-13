#! /user/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector
from datetime import date, datetime

titles = ['爱娃.布劳恩，希特勒背后的女人|纪录片',
          '今天被人加塞了，但是我却撞了上去',
          '悲报：13年过去，道明寺家族资产大幅缩水',
          '百货50条，全部是实用的玩意儿（07.11）',
          '微语录精选0711：据说辣也是痛的一种'
          ]
summary = ['爱娃.布劳恩是德国慕尼黑人。1929年，17岁的她在海因里希·霍夫曼的照相店中工作，帮助售货、照相和冲洗照片。当时霍夫曼是纳粹党元首阿道夫·希特勒的专用摄影师。由此，她认识了阿道夫.希特勒，并逐渐与其发展成恋爱关系，长期...',
           '今日楼主所在的城市因为要搞省运会主干道开始修路，导致楼主下班回家的那条路异常拥堵，当楼主慢慢的在左拐道等红灯的时候，就看见前面有不少加塞的，其实开车的都有这种感觉，加塞的太可恨了。当我起步的时候，突然从左侧加塞进来一辆S...',
           '昨晚新版《流星花园》首播，网友们神吐槽成了新的快乐源泉[偷笑]进度快，#郭采洁#台词略中二，F4集体变学霸，道明寺竟还是金融界学霸（说好的不会算数呢[摊手]）？道明寺拿外卖打杉菜？花泽类突然倒立，还亲了杉菜；道明寺表白杉...',
           '【龙之艺不锈钢刀具套组六件套49元】此款龙之艺不锈钢刀具套组采用4cr13mov不锈钢制作，防腐防锈，坚固耐用，刀身刀柄一体，永不脱落，使用安全，套刀包括：斩骨刀18cm，切片刀17cm，水果刀12.5cm，磨刀棒，厨房...',
           '20岁的时候，下雨了，你希望你男人可以在暴雨中跟你热烈拥吻；40岁的时候，下雨了，你希望你男人可以想起来外面还晾着衣服。——tweetletitixiang译​手机的平均寿命只有2～3年，手机活一年相当于人类活三十年，请...',
           ]
category = ['视频', '文摘', '文摘', '优惠', '文摘']
author = ['梁萧', '梁萧', '梁萧', '梁萧', '梁萧']
image_count = [1, 4, 2, 140, 1]

relations = {1: ['希特勒'], 2: ['车加塞', '车祸'], 3: ['流星花园' '道明寺'], 4: ['微语录'], 5: ['段子']}

tags = ['希特勒', '车加塞', '车祸', '流星花园' '道明寺', '微语录', '段子']

cnx = mysql.connector.connect(user='root', password='cute', database='storysite')
cursor = cnx.cursor()


def add_article():
    add_entry = ('INSERT INTO article (title, summary, category, author, image_count, pub_date) VALUES (%s, %s, %s, %s, %s, %s)')
    for i in range(5):
        entry = (titles[i], summary[i], category[i], author[i], image_count[i], datetime.now())
        cursor.execute(add_entry, entry)
        print 'insert finish:%d' % i

    cnx.commit()

    cursor.close()
    cnx.close()


def add_tag():
    sql = "INSERT INTO tag (tag) VALUES (%(tag)s)"
    for i in range(len(tags)):
        cursor.execute(sql, {'tag': tags[i]})
        print 'insert:%s' % tags[i]

    cnx.commit()
    cursor.close()


def bindTags():
    cursor.execute("SELECT articleId FROM article")
    results = cursor.fetchall()

    sql = ('INSERT INTO article_tags (article_id, tag_id) VALUES (%s, %s)')

    for row in results:
        articleId = row[0]
        tags = relations[articleId]

        for t in tags:
            cursor.execute(sql, (articleId, t))
            print 'insert %s' % t

    cnx.commit()
    cursor.close()


if __name__ == '__main__':
    bindTags()

