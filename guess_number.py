"""
猜数字游戏 —— Python 入门练手项目

游戏规则：
  程序随机生成一个 1~100 之间的整数
  玩家输入猜测，程序提示「大了」「小了」
  猜中后显示猜测次数
"""

import random


def 猜数字游戏():
    """主游戏逻辑"""
    print("=" * 40)
    print("🎯 猜数字游戏")
    print("  我心里想了一个 1~100 之间的数，来猜猜看！")
    print("=" * 40)

    目标数字 = random.randint(1, 100)
    猜测次数 = 0

    while True:
        try:
            玩家输入 = input("\n🔢 请输入你猜的数字（1~100）：").strip()
            if 玩家输入.lower() == "q":
                print(f"👋 游戏结束！正确数字是 {目标数字}。下次再来挑战！")
                break

            猜测 = int(玩家输入)
            if 猜测 < 1 or 猜测 > 100:
                print("⚠️  请输入 1~100 之间的数字！")
                continue

            猜测次数 += 1

            if 猜测 < 目标数字:
                print("📉 太小了！再大一点～")
            elif 猜测 > 目标数字:
                print("📈 太大了！再小一点～")
            else:
                print(f"\n🎉 恭喜你猜中了！正确数字就是 {目标数字}！")
                print(f"📊 你一共猜了 {猜测次数} 次。")

                # 评价
                if 猜测次数 <= 3:
                    print("🌟 评价：你是天才！")
                elif 猜测次数 <= 7:
                    print("👍 评价：还不错！")
                else:
                    print("💪 评价：多练练会更好！")
                break

        except ValueError:
            print("⚠️  输入无效！请输入一个整数，输入 q 退出。")


if __name__ == "__main__":
    猜数字游戏()
