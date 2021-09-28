urls = [
        "[软技能:代码之外的生存指南](https://book.douban.com/subject/26835090)",
        "[深入理解 Java 虚拟机](https://book.douban.com/subject/34907497)",
        "[编程之道](https://book.douban.com/subject/1899158)",
        "[现代操作系统](https://book.douban.com/subject/27096665)",
        "[MyBatis 技术内幕](https://book.douban.com/subject/27087564)",
        "[字母表谜案](https://book.douban.com/subject/35390390)",
        "[心灵侦探城塚翡翠](https://book.douban.com/subject/35296788)",
        "[诡计博物馆](https://book.douban.com/subject/35016085)",
        "[金色麦田](https://book.douban.com/subject/33404959)",
        "[嫌疑人 X 的献身](https://book.douban.com/subject/3211779)",
        "[Operating Systems: Three Easy Pieces](https://book.douban.com/subject/34994608)",
        "[绝对不在场证明](https://book.douban.com/subject/34998167)",
        "[乌合之众](https://book.douban.com/subject/1012611)",
        "[尸体变化图鉴](https://book.douban.com/subject/30264678)",
        "[密室收藏家](https://book.douban.com/subject/26348596)",
        "[数据密集型应用系统设计](https://book.douban.com/subject/30329536)",
        "[活着](https://book.douban.com/subject/4913064)",
        "[许三观卖血记](https://book.douban.com/subject/1029791)",
        "[MySQL 技术内幕](https://book.douban.com/subject/24708143)",
        "[被讨厌的勇气](https://book.douban.com/subject/26369699)",
        "[计算机网络自顶向下方法](https://book.douban.com/subject/30280001)",
        "[恶意](https://book.douban.com/subject/26877752)",
        "[不正经的魔术讲师与禁忌教典 ロクでなし魔術講師と禁忌教典 (2017)](https://movie.douban.com/subject/26774749)",
        "[幼女战记 幼女戦記 (2017)](https://movie.douban.com/subject/26720121)",
        "[暗金丑岛君 第一季 闇金ウシジマくん (2010)](https://movie.douban.com/subject/4851891)",
        "[经济机器是如何运行的（2008）](https://movie.douban.com/subject/30458820)",
        "[鱿鱼游戏 오징어 게임 (2021)](https://movie.douban.com/subject/34812928)",
        "[失控玩家 Free Guy (2021)](https://movie.douban.com/subject/30337388)",
        "[911：总统作战室 9/11: Inside the President’s War Room (2021)](https://movie.douban.com/subject/35576386)",
        "[自卫的艺术 The Art of Self-Defense (2019)](https://movie.douban.com/subject/27138615)",
        "[X 特遣队：全员集结 The Suicide Squad (2021)](https://movie.douban.com/subject/26741632)",
        "[洛基 第一季 Loki Season 1 (2021)](https://movie.douban.com/subject/30331432)",
        "[猎鹰与冬兵 The Falcon and the Winter Soldier (2021)](https://movie.douban.com/subject/30367642)",
        "[哥斯拉大战金刚 Godzilla vs Kong (2021)](https://movie.douban.com/subject/26613692)",
        "[不眠 Vigil (2021)](https://movie.douban.com/subject/34953711)",
        "[全职猎人 2011 HUNTER×HUNTER (2011)](https://movie.douban.com/subject/6748086)",
        "[关于我转生变成史莱姆这档事 第二季 (2021)](https://movie.douban.com/subject/27186493)",
        "[扎克·施奈德版正义联盟 Zack Snyder's Justice League (2021)](https://movie.douban.com/subject/35076714)",
        "[无职转生：到了异世界就拿出真本事 (2021)](https://movie.douban.com/subject/30513783)",
        "[伍六七之玄武国篇 (2021)](https://movie.douban.com/subject/35161255)",
        "[我的英雄学院 第 5 季 (2021)](https://movie.douban.com/subject/35235594)",
        "[鬼灭之刃 剧场版 无限列车篇 (2020)](https://movie.douban.com/subject/34845781)"]

if __name__ == '__main__':
    col = 8
    print('|'*(col-0))
    print(*['|' for i in range(col)], sep=':-:')
    i = 0
    while i < len(urls):
        j = i
        tmp = []
        lines = urls[i:i+col]
        for line in lines:
            t, u = line.split('](')
            n = '[!'+t + ']('+'../../douban/' + u.split('/')[-1][0:-1] + \
                ('.png'if 'book' in u else '.webp')+')]'+'('+u
            tmp.append(n)
        print(*tmp, sep='|', end='|')
        print()
        i += col
