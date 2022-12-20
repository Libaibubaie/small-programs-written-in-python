import hashlib 
import base64
while True:
    #加密数
    string = input("请输入(若要退出请打[e]）:");
    if string == "e":
        break
    #选择模式
    mode = input("[a]sha,md5,base64 [b]ECC椭圆曲线加密 [c]便于解密 [d]解密c [e]凯撒加密/解密:");
    if mode == "a":

        
        #将ascill码加1
        news = ''
        for i in string:
            if i == " ":
                news = news + i
            else:
                news = news + chr(ord(i) + 1)
        print("1次加密结果:",news)

        #将字符串反向
        news2 = (news[::-1])
        print("2次加密结果:",news2)

        #再一次增加ascill码
        string = news2
        news3 = ''
        for i in string:
            if i == " ":
                news3 = news3 + i
            else:
                news3 = news3 + chr(ord(i) + 1)
        print("3次加密结果:",news3)
        #MD5加密
        string=news3
        md5 = hashlib.md5()  
        md5.update(string.encode('utf-8'))#转码，update里的必须是字节型 
        res = md5.hexdigest() #返回字符型摘要信息 
        print(md5.digest())#返回字节型的摘要信息 
        print("md5加密结果:",res) 

        #sha256加密
        string=news3
        sha256 = hashlib.sha256() 
        sha256.update(string.encode('utf-8')) 
        res = sha256.hexdigest() 
        print("sha256加密结果:",res) 

        #sha512
        string=news3
        sha512= hashlib.sha512() 
        sha512.update(string.encode('utf-8')) 
        res = sha512.hexdigest() 
        print("sha512加密结果:",res) 

    if mode == "b":
                


        # -*- coding:utf-8 *-
        # author: DYBOY
        # reference codes: https://blog.dyboy.cn/websecurity/121.html
        # description: ECC椭圆曲线加密算法实现
        """
            考虑K=kG ，其中K、G为椭圆曲线Ep(a,b)上的点，n为G的阶（nG=O∞ ），k为小于n的整数。
            则给定k和G，根据加法法则，计算K很容易但反过来，给定K和G，求k就非常困难。
            因为实际使用中的ECC原则上把p取得相当大，n也相当大，要把n个解点逐一算出来列成上表是不可能的。
            这就是椭圆曲线加密算法的数学依据
            点G称为基点（base point）
            k（k<n）为私有密钥（privte key）
            K为公开密钥（public key)
        """

        def get_inverse(mu, p):
            """
            获取y的负元
            """
            for i in range(1, p):
                if (i*mu)%p == 1:
                    return i
            return -1

        def get_gcd(zi, mu):
            """
            获取最大公约数
            """
            if mu:
                return get_gcd(mu, zi%mu)
            else:
                return zi

        def get_np(x1, y1, x2, y2, a, p):
            """
            获取n*p，每次+p，直到求解阶数np=-p
            """
            flag = 1  # 定义符号位（+/-）

            # 如果 p=q  k=(3x2+a)/2y1mod p
            if x1 == x2 and y1 == y2:
                zi = 3 * (x1 ** 2) + a  # 计算分子      【求导】
                mu = 2 * y1    # 计算分母

            # 若P≠Q，则k=(y2-y1)/(x2-x1) mod p
            else:
                zi = y2 - y1
                mu = x2 - x1
                if zi* mu < 0:
                    flag = 0        # 符号0为-（负数）
                    zi = abs(zi)
                    mu = abs(mu)

            # 将分子和分母化为最简
            gcd_value = get_gcd(zi, mu)     # 最大公約數
            zi = zi // gcd_value            # 整除
            mu = mu // gcd_value
            # 求分母的逆元  逆元： ∀a ∈G ，ョb∈G 使得 ab = ba = e
            # P(x,y)的负元是 (x,-y mod p)= (x,p-y) ，有P+(-P)= O∞
            inverse_value = get_inverse(mu, p)
            k = (zi * inverse_value)

            if flag == 0:                   # 斜率负数 flag==0
                k = -k
            k = k % p
            # 计算x3,y3 P+Q
            """
                x3≡k2-x1-x2(mod p)
                y3≡k(x1-x3)-y1(mod p)
            """
            x3 = (k ** 2 - x1 - x2) % p
            y3 = (k * (x1 - x3) - y1) % p
            return x3,y3

        def get_rank(x0, y0, a, b, p):
            """
            获取椭圆曲线的阶
            """
            x1 = x0             #-p的x坐标
            y1 = (-1*y0)%p      #-p的y坐标
            tempX = x0
            tempY = y0
            n = 1
            while True:
                n += 1
                # 求p+q的和，得到n*p，直到求出阶
                p_x,p_y = get_np(tempX, tempY, x0, y0, a, p)
                # 如果 == -p,那么阶数+1，返回
                if p_x == x1 and p_y == y1:
                    return n+1
                tempX = p_x
                tempY = p_y

        def get_param(x0, a, b, p):
            """
            计算p与-p
            """
            y0 = -1
            for i in range(p):
                # 满足取模约束条件，椭圆曲线Ep(a,b)，p为质数，x,y∈[0,p-1]
                if i**2%p == (x0**3 + a*x0 + b)%p:
                    y0 = i
                    break

            # 如果y0没有，返回false
            if y0 == -1:
                return False

            # 计算-y（负数取模）
            x1 = x0
            y1 = (-1*y0) % p
            return x0,y0,x1,y1

        def get_graph(a, b, p):
            """
            输出椭圆曲线散点图
            """
            x_y = []
            # 初始化二维数组
            for i in range(p):
                x_y.append(['-' for i in range(p)])

            for i in range(p):
                val =get_param(i, a, b, p)  # 椭圆曲线上的点
                if(val != False):
                    x0,y0,x1,y1 = val
                    x_y[x0][y0] = 1
                    x_y[x1][y1] = 1

            print("椭圆曲线的散列图为：")
            for i in range(p):              # i= 0-> p-1
                temp = p-1-i        # 倒序

                # 格式化输出1/2位数，y坐标轴
                if temp >= 10:
                    print(temp, end=" ")
                else:
                    print(temp, end="  ")

                # 输出具体坐标的值，一行
                for j in range(p):
                    print(x_y[j][temp], end="  ")
                print("")   #换行

            # 输出 x 坐标轴
            print("  ", end="")
            for i in range(p):
                if i >=10:
                    print(i, end=" ")
                else:
                    print(i, end="  ")
            print('\n')

        def get_ng(G_x, G_y, key, a, p):
            """
            计算nG
            """
            temp_x = G_x
            temp_y = G_y
            while key != 1:
                temp_x,temp_y = get_np(temp_x,temp_y, G_x, G_y, a, p)
                key -= 1
            return temp_x,temp_y

        def ecc_main():
            while True:
                a = int(input("请输入椭圆曲线参数a(a>0)的值："))
                b = int(input("请输入椭圆曲线参数b(b>0)的值："))
                p = int(input("请输入椭圆曲线参数p(p为素数)的值："))   #用作模运算

                # 条件满足判断
                if (4*(a**3)+27*(b**2))%p == 0:
                    print("您输入的参数有误，请重新输入！！！\n")
                else:
                    break

            # 输出椭圆曲线散点图
            get_graph(a, b, p)

            # 选点作为G点
            print("user1：在如上坐标系中选一个值为G的坐标")
            G_x = int(input("user1：请输入选取的x坐标值："))
            G_y = int(input("user1：请输入选取的y坐标值："))

            # 获取椭圆曲线的阶
            n = get_rank(G_x, G_y, a, b, p)

            # user1生成私钥，小key
            key = int(input("user1：请输入私钥小key（<{}）：".format(n)))

            # user1生成公钥，大KEY
            KEY_x,kEY_y = get_ng(G_x, G_y, key, a, p)

            # user2阶段
            # user2拿到user1的公钥KEY，Ep(a,b)阶n，加密需要加密的明文数据
            # 加密准备
            k = int(input("user2：请输入一个整数k（<{}）用于求kG和kQ：".format(n)))
            k_G_x,k_G_y = get_ng(G_x, G_y, k, a, p)                         # kG
            k_Q_x,k_Q_y = get_ng(KEY_x, kEY_y, k, a, p)                     # kQ

            # 加密
            plain_text = string
            plain_text = plain_text.strip()
            #plain_text = int(input("user1：请输入需要加密的密文："))
            c = []
            print("密文为：",end="")
            for char in plain_text:
                intchar = ord(char)
                cipher_text = intchar*k_Q_x
                c.append([k_G_x, k_G_y, cipher_text])
                print("({},{}),{}".format(k_G_x, k_G_y, cipher_text),end="-")


            # user1阶段
            # 拿到user2加密的数据进行解密
            # 知道 k_G_x,k_G_y，key情况下，求解k_Q_x,k_Q_y是容易的，然后plain_text = cipher_text/k_Q_x
            print("\nuser1解密得到明文：",end="")
            for charArr in c:
                decrypto_text_x,decrypto_text_y = get_ng(charArr[0], charArr[1], key, a, p)
                print(chr(charArr[2]//decrypto_text_x),end="")

        if __name__ == "__main__":
            print("*************ECC椭圆曲线加密*************")
            ecc_main()

    if mode =="c":
        result = ""
        # 加密过程
        # 遍历字符串，转换成数字
        for char in string:
            num = ord(char)
            result += str(num) + "|" # 结果用竖线分割
        print("加密后的数据:" + result)

    if mode == "d":
        result1 = input("输入加密过的：")
        # 解密过程
        # 把加密后的数据转换成列表
        result_list = result1.split("|")
        # 移除列表中最后一个空字符
        result_list.remove("")
        print("密文列表:" + str(result_list))

        # 遍历列表，转换成字符
        # 存储解密后的数据
        after_message = ""
        for index in result_list:
            int_index = int(index)
            after_message += chr(int_index) # 将字符链接成字符串
        print("解密后的结果：" + after_message)
    #凯撒加密解密
    if mode == "e":
        str = string
        key = int(input("请输入密钥："))
        enc = int(input("0 - 解密\n1 - 加密\n请选择 0 或者 1: "))
        str_enc = ""
        str_dec = ""

        if enc == 1:  #加密
            for i in str:  #用i进行遍历
                if i.isupper():  #isupper函数判断i是否为大写字母
                    i_unicode = ord(i)  #找到“i”对应的Unicode码
                    i_index = ord(i) - ord("A")  #计算字母“i”到A（起始）的间距
                    new_index = (i_index + key) % 26
                    new_unicode = new_index + ord("A")
                    new_character = chr(new_unicode)  #将Unicode码转换为字符
                    str_enc += new_character
                elif i.islower():  #如果“i”为小写字母
                    i_unicode = ord(i)
                    i_index = ord(i) - ord("a")
                    new_index = (i_index + key) % 26
                    new_unicode = new_index + ord("a")
                    new_character = chr(new_unicode)
                    str_enc = str_enc + new_character
                else:  #数字或符号
                    str_enc += i  #直接返回“i”
            print("密文为：",str_enc)

        else:  #解密
            for k in str:
                if k.isupper():
                    k_unicode = ord(k)
                    k_index = ord(k) - ord("A")
                    new_index = (k_index - key) % 26
                    new_unicode = new_index + ord("A")
                    new_character = chr(new_unicode)
                    str_dec = str_dec + new_character
                elif k.islower():
                    k_unicode = ord(k)
                    k_index = ord(k) - ord("a")
                    new_index = (k_index - key) % 26
                    new_unicode = new_index + ord("a")
                    new_character = chr(new_unicode)
                    str_dec += new_character 
                else:
                    str_dec += k
            print("明文为：",str_dec)

    print("/n")
    print("--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---")