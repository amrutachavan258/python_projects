def calculate_love(name1,name2):
    combine_name=(name1+name2).lower()
    true_score=(
        combine_name.count("t")+
        combine_name.count("r")+
        combine_name.count("u")+
        combine_name.count("e")
    )
    love_score=(
        combine_name.count("l")+
        combine_name.count("o")+
        combine_name.count("v")+
        combine_name.count("e")
    )

    total=str(true_score)+str(love_score)
    print(total)
calculate_love("riya","yash")