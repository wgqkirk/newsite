function fun1(){
    var list0=''
    for(var i=0;i<$('#week1 tr').length-1;i++){
        var uid = $("#week1>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week1 tr').length-1;i++){
        var name = $("#week1>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week1 tr').length-1;i++){
        var weight = $("#week1>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)

    var list3=''
    for(var i=0;i<$('#week1 tr').length-1;i++){
        var beizhu = $("#week1>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)
    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week1',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun2(){
    var list0=''
    for(var i=0;i<$('#week2 tr').length-1;i++){
        var uid = $("#week2>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week2 tr').length-1;i++){
        var name = $("#week2>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week2 tr').length-1;i++){
        var weight = $("#week2>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)
    var list3=''
    for(var i=0;i<$('#week2 tr').length-1;i++){
        var beizhu = $("#week2>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)
    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week2',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun3(){
    var list0=''
    for(var i=0;i<$('#week3 tr').length-1;i++){
        var uid = $("#week3>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week3 tr').length-1;i++){
        var name = $("#week3>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week3 tr').length-1;i++){
        var weight = $("#week3>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)

    var list3=''
    for(var i=0;i<$('#week3 tr').length-1;i++){
        var beizhu = $("#week3>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)
    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week3',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun4(){
    var list0=''
    for(var i=0;i<$('#week4 tr').length-1;i++){
        var uid = $("#week4>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week4 tr').length-1;i++){
        var name = $("#week4>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week4 tr').length-1;i++){
        var weight = $("#week4>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)
    var list3=''
    for(var i=0;i<$('#week4 tr').length-1;i++){
        var beizhu = $("#week4>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)

    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week4',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun5(){
    var list0=''
    for(var i=0;i<$('#week5 tr').length-1;i++){
        var uid = $("#week5>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week5 tr').length-1;i++){
        var name = $("#week5>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week5 tr').length-1;i++){
        var weight = $("#week5>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)
    var list3=''
    for(var i=0;i<$('#week5 tr').length-1;i++){
        var beizhu = $("#week5>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)

    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week5',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun6(){
    var list0=''
    for(var i=0;i<$('#week6 tr').length-1;i++){
        var uid = $("#week6>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week6 tr').length-1;i++){
        var name = $("#week6>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week6 tr').length-1;i++){
        var weight = $("#week6>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)
    var list3=''
    for(var i=0;i<$('#week6 tr').length-1;i++){
        var beizhu = $("#week6>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)

    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week6',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun7(){
    var list0=''
    for(var i=0;i<$('#week7 tr').length-1;i++){
        var uid = $("#week7>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week7 tr').length-1;i++){
        var name = $("#week7>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week7 tr').length-1;i++){
        var weight = $("#week7>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)
    var list3=''
    for(var i=0;i<$('#week7 tr').length-1;i++){
        var beizhu = $("#week7>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)

    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week7',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}

function fun8(){
    var list0=''
    for(var i=0;i<$('#week8 tr').length-1;i++){
        var uid = $("#week8>tbody>tr:eq("+i+")>#uid>input").val();
        list0 += uid+"#";
    }
    list0=list0.substring(0,list0.length-1);
    console.log(list0)


    var list1=''
    for(var i=0;i<$('#week8 tr').length-1;i++){
        var name = $("#week8>tbody>tr:eq("+i+")>#username>input").val();
        list1 += "\""+name+"\"#";
    }
    list1=list1.substring(0,list1.length-1);
    console.log(list1)

    var list2=''
    for(var i=0;i<$('#week8 tr').length-1;i++){
        var weight = $("#week8>tbody>tr:eq("+i+")>#weight>input").val();
        list2 += weight+"#";
    }
    list2=list2.substring(0,list2.length-1);
    console.log(list2)
    var list3=''
    for(var i=0;i<$('#week8 tr').length-1;i++){
        var beizhu = $("#week8>tbody>tr:eq("+i+")>#beizhu>input").val();
        list3 += beizhu+"#";
    }
    list3=list3.substring(0,list3.length-1);
    console.log(list3)

    var choice=confirm('确认修改?')
    if (choice){
        $.ajax({
            url:'/coach_inputdata/',
            data:{userid:list0,weight:list2,FieldName:'week8',beizhu:list3},
            type:'POST',
            success:function (data) {
                console.log(data)
                window.location.reload()
            }
        })
    }

}
