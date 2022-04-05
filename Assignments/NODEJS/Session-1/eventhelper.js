const EventEmitter = require("events")

class EventHelper extends EventEmitter{
    triggerEvent(logs){
        this.emit("LogRecorded", {currentlog: logs})
    }
}
module.exports= EventHelper;