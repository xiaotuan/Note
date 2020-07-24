**Log.js**

```js
var ALLlOG = true                      // 是否允许打印所有日志
var LOCAL = ALLlOG && true             // 是否允许打印本地日志
var REMOTE = ALLlOG && false            // 是否打印实时日志
var DEBUG = ALLlOG && true             // 是否允许打印本地调试日志
var INFO = ALLlOG && true              // 是否允许打印本地信息日志
var WARN = ALLlOG && true              // 是否允许打印本地警告日志
var ERROR = ALLlOG && true             // 是否允许打印本地错误日志

var log = wx.getRealtimeLogManager ? wx.getRealtimeLogManager() : null

function formatArguments(args) {
  if (args && args.length >= 2) {
    var first = args[0]
    var second = args[1]
    var msg = logTime() + " [" + first + "] " + second
    for (var i = 2; i < args.length; i++) {
      if (typeof(args[i]) == 'object') {
        msg += JSON.stringify(args[i])
      } else {
        msg += args[i]
      }
    }
    return msg
  } else if (args && args.length === 1) {
    if (typeof(args[i]) == 'object') {
      return logTime() + " [" + JSON.stringify(args[0]) + "] "
    } else {
      return logTime() + " [" + args[0] + "] "
    }
  }
  return ""
}

function logTime() {
  var date = new Date()
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()
  const millsecond = date.getMilliseconds()

  return [year, month, day].map(formatNumber).join('-') + ' ' + [hour, minute, second].map(formatNumber).join(':') + " " + formatMillSecond(millsecond)
}

function formatNumber(n) {
  n = n.toString()
  return n[1] ? n : '0' + n
}

function formatMillSecond(n) {
  n = n.toString()
  return n[2] ? n : n[1] ? '0' + n : '00' + n
}

module.exports = {

  d() {
    if (DEBUG) {
      if (REMOTE) {
        log.debug.apply(log, arguments)
      }
      if (LOCAL) {
        var msg = formatArguments(arguments);
        console.debug(msg)
      }
    }
  },

  i() {
    if (INFO) {
      if (REMOTE) {
        log.info.apply(log, arguments)
      }
      if (LOCAL) {
        var msg = formatArguments(arguments);
        console.debug(msg)
      }
    }
  },

  w() {
    if (WARN) {
      if (REMOTE) {
        log.warn.apply(log, arguments)
      }
      if (LOCAL) {
        var msg = formatArguments(arguments);
        console.debug(msg)
      }
    }
  },

  e() {
    if (ERROR) {
      if (REMOTE) {
        log.error.apply(log, arguments)
      }
      if (LOCAL) {
        var msg = formatArguments(arguments);
        console.debug(msg)
      }
    }
  },

  setFilterMsg(msg) { // 从基础库2.7.3开始支持
    if (!log || !log.setFilterMsg) return
    if (typeof msg !== 'string') return
    log.setFilterMsg(msg)
  },

  addFilterMsg(msg) { // 从基础库2.8.1开始支持
    if (!log || !log.addFilterMsg) return
    if (typeof msg !== 'string') return
    log.addFilterMsg(msg)
  },

}
```

