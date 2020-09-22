from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

#taks2 add json instruction
instructions = [{
  "id": 1,
  "name": "Paint a wall",
  "description": "Instructions how to paint a wall",
  "steps": [" Clean the wall", "Tape the trim",
    "Roll the primer onto the wall",
    "Paint the trim", "Remove the painter's tape"],
    "tools": ["painter's tape", "primer", "paint", "paint roller",
    "paint tray", " paintbrush"],
  "cost": 100,
  "duration": 8},

  {"id": 2,
  "name": "Repair the House",
  "description": "Instructions how to repair the house",
  "steps": [" Repair the taps", "Repair electricals",
    "Change old carpets and curtains",
    "Fix wall papers"],
    "tools": ["Toolsets", "Plumbing toolsets", "carpets and curtains",
    "chairs and tables", " vehicles"],
  "cost": 800,
  "duration": 24
}];


#task3a, get all instructions
@app.route('/instructions', methods=['GET'])
def get_instructions():
    #print ( jsonify({'data': instructions}))
    return (jsonify({'data': instructions}))

#task3b, display instruction by id
@app.route('/instructions/<int:id>', methods=['GET'])
def get_recipe(id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == id), None)

    if instruction:
        return jsonify(instruction)

    return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND

#task3c, create new instruction
@app.route('/instructions', methods=['POST'])
def create_instruction():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')

    instruction = {
        'id': len(instructions) + 1,
        'name': name,
        'description': description
    }

    instructions.append(instruction)

    return jsonify(instruction), HTTPStatus.CREATED

#task3d, modify instruction
@app.route('/instructions/<int:id>', methods=['PUT'])
def update_instruction(id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == id), None)

    if not instruction:
        return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    instruction.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )

    return jsonify(instruction)

#Task3e, delete instruction
@app.route('/instructions/<int:id>', methods=['DELETE'])
def delete_instruction(id):
  instruction = next((instruction for instruction in instructions if instruction['id'] == id), None)
  if not instruction:
    return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND
  instructions.remove(instruction)
  return '', HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run()