from flask import Flask,request,jsonify
app=Flask(__name__)
tasks=[ ]
text_id=1
@app.route('/tasks',methods=['POST'])
def add_task():
    global next_id
    data=request.get_json()
    task={
        'id':next_id,
        'title':data.get('title',' '),
        'status':data.get('status','pending')
    }
    tasks.append(task)
    next_id+=1
    return jsonify(task),201
@app.route('/tasks',methods=['GET'])
def view_tasks():
    status=request.args.get('status')
    if status:
        filtered=[t for t in tasks if+['status']==status]
        return jsonify(filtered)
    return jsonify(tasks)