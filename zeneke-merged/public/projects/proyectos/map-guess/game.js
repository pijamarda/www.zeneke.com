
var Module;

if (typeof Module === 'undefined') Module = eval('(function() { try { return Module || {} } catch(e) { return {} } })()');

if (!Module.expectedDataFileDownloads) {
  Module.expectedDataFileDownloads = 0;
  Module.finishedDataFileDownloads = 0;
}
Module.expectedDataFileDownloads++;
(function() {
 var loadPackage = function(metadata) {

    var PACKAGE_PATH;
    if (typeof window === 'object') {
      PACKAGE_PATH = window['encodeURIComponent'](window.location.pathname.toString().substring(0, window.location.pathname.toString().lastIndexOf('/')) + '/');
    } else if (typeof location !== 'undefined') {
      // worker
      PACKAGE_PATH = encodeURIComponent(location.pathname.toString().substring(0, location.pathname.toString().lastIndexOf('/')) + '/');
    } else {
      throw 'using preloaded data can only be done on a web page or in a web worker';
    }
    var PACKAGE_NAME = 'game.data';
    var REMOTE_PACKAGE_BASE = 'game.data';
    if (typeof Module['locateFilePackage'] === 'function' && !Module['locateFile']) {
      Module['locateFile'] = Module['locateFilePackage'];
      Module.printErr('warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)');
    }
    var REMOTE_PACKAGE_NAME = typeof Module['locateFile'] === 'function' ?
                              Module['locateFile'](REMOTE_PACKAGE_BASE) :
                              ((Module['filePackagePrefixURL'] || '') + REMOTE_PACKAGE_BASE);
  
    var REMOTE_PACKAGE_SIZE = metadata.remote_package_size;
    var PACKAGE_UUID = metadata.package_uuid;
  
    function fetchRemotePackage(packageName, packageSize, callback, errback) {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', packageName, true);
      xhr.responseType = 'arraybuffer';
      xhr.onprogress = function(event) {
        var url = packageName;
        var size = packageSize;
        if (event.total) size = event.total;
        if (event.loaded) {
          if (!xhr.addedTotal) {
            xhr.addedTotal = true;
            if (!Module.dataFileDownloads) Module.dataFileDownloads = {};
            Module.dataFileDownloads[url] = {
              loaded: event.loaded,
              total: size
            };
          } else {
            Module.dataFileDownloads[url].loaded = event.loaded;
          }
          var total = 0;
          var loaded = 0;
          var num = 0;
          for (var download in Module.dataFileDownloads) {
          var data = Module.dataFileDownloads[download];
            total += data.total;
            loaded += data.loaded;
            num++;
          }
          total = Math.ceil(total * Module.expectedDataFileDownloads/num);
          if (Module['setStatus']) Module['setStatus']('Downloading data... (' + loaded + '/' + total + ')');
        } else if (!Module.dataFileDownloads) {
          if (Module['setStatus']) Module['setStatus']('Downloading data...');
        }
      };
      xhr.onload = function(event) {
        var packageData = xhr.response;
        callback(packageData);
      };
      xhr.send(null);
    };

    function handleError(error) {
      console.error('package error:', error);
    };
  
      var fetched = null, fetchedCallback = null;
      fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE, function(data) {
        if (fetchedCallback) {
          fetchedCallback(data);
          fetchedCallback = null;
        } else {
          fetched = data;
        }
      }, handleError);
    
  function runWithFS() {

    function assert(check, msg) {
      if (!check) throw msg + new Error().stack;
    }
Module['FS_createPath']('/', '.git', true, true);
Module['FS_createPath']('/.git', 'info', true, true);
Module['FS_createPath']('/.git', 'hooks', true, true);
Module['FS_createPath']('/.git', 'objects', true, true);
Module['FS_createPath']('/.git/objects', 'b9', true, true);
Module['FS_createPath']('/.git/objects', '63', true, true);
Module['FS_createPath']('/.git/objects', 'e5', true, true);
Module['FS_createPath']('/.git/objects', '84', true, true);
Module['FS_createPath']('/.git/objects', '62', true, true);
Module['FS_createPath']('/.git/objects', 'b4', true, true);
Module['FS_createPath']('/.git/objects', '0e', true, true);
Module['FS_createPath']('/.git/objects', '87', true, true);
Module['FS_createPath']('/.git/objects', '78', true, true);
Module['FS_createPath']('/.git/objects', '7c', true, true);
Module['FS_createPath']('/.git/objects', '9f', true, true);
Module['FS_createPath']('/.git/objects', '06', true, true);
Module['FS_createPath']('/.git/objects', '42', true, true);
Module['FS_createPath']('/.git/objects', '96', true, true);
Module['FS_createPath']('/.git/objects', '1c', true, true);
Module['FS_createPath']('/.git/objects', 'e4', true, true);
Module['FS_createPath']('/.git/objects', '75', true, true);
Module['FS_createPath']('/.git/objects', '14', true, true);
Module['FS_createPath']('/.git/objects', 'da', true, true);
Module['FS_createPath']('/.git/objects', '5f', true, true);
Module['FS_createPath']('/.git', 'refs', true, true);
Module['FS_createPath']('/.git/refs', 'heads', true, true);
Module['FS_createPath']('/.git/refs', 'remotes', true, true);
Module['FS_createPath']('/.git/refs/remotes', 'origin', true, true);
Module['FS_createPath']('/.git', 'logs', true, true);
Module['FS_createPath']('/.git/logs', 'refs', true, true);
Module['FS_createPath']('/.git/logs/refs', 'heads', true, true);
Module['FS_createPath']('/.git/logs/refs', 'remotes', true, true);
Module['FS_createPath']('/.git/logs/refs/remotes', 'origin', true, true);
Module['FS_createPath']('/', 'assets', true, true);
Module['FS_createPath']('/assets', 'img', true, true);

    function DataRequest(start, end, crunched, audio) {
      this.start = start;
      this.end = end;
      this.crunched = crunched;
      this.audio = audio;
    }
    DataRequest.prototype = {
      requests: {},
      open: function(mode, name) {
        this.name = name;
        this.requests[name] = this;
        Module['addRunDependency']('fp ' + this.name);
      },
      send: function() {},
      onload: function() {
        var byteArray = this.byteArray.subarray(this.start, this.end);

          this.finish(byteArray);

      },
      finish: function(byteArray) {
        var that = this;

        Module['FS_createDataFile'](this.name, null, byteArray, true, true, true); // canOwn this data in the filesystem, it is a slide into the heap that will never change
        Module['removeRunDependency']('fp ' + that.name);

        this.requests[this.name] = null;
      },
    };

        var files = metadata.files;
        for (i = 0; i < files.length; ++i) {
          new DataRequest(files[i].start, files[i].end, files[i].crunched, files[i].audio).open('GET', files[i].filename);
        }

  
    function processPackageData(arrayBuffer) {
      Module.finishedDataFileDownloads++;
      assert(arrayBuffer, 'Loading data file failed.');
      assert(arrayBuffer instanceof ArrayBuffer, 'bad input to processPackageData');
      var byteArray = new Uint8Array(arrayBuffer);
      var curr;
      
        // copy the entire loaded file into a spot in the heap. Files will refer to slices in that. They cannot be freed though
        // (we may be allocating before malloc is ready, during startup).
        if (Module['SPLIT_MEMORY']) Module.printErr('warning: you should run the file packager with --no-heap-copy when SPLIT_MEMORY is used, otherwise copying into the heap may fail due to the splitting');
        var ptr = Module['getMemory'](byteArray.length);
        Module['HEAPU8'].set(byteArray, ptr);
        DataRequest.prototype.byteArray = Module['HEAPU8'].subarray(ptr, ptr+byteArray.length);
  
          var files = metadata.files;
          for (i = 0; i < files.length; ++i) {
            DataRequest.prototype.requests[files[i].filename].onload();
          }
              Module['removeRunDependency']('datafile_game.data');

    };
    Module['addRunDependency']('datafile_game.data');
  
    if (!Module.preloadResults) Module.preloadResults = {};
  
      Module.preloadResults[PACKAGE_NAME] = {fromCache: false};
      if (fetched) {
        processPackageData(fetched);
        fetched = null;
      } else {
        fetchedCallback = processPackageData;
      }
    
  }
  if (Module['calledRun']) {
    runWithFS();
  } else {
    if (!Module['preRun']) Module['preRun'] = [];
    Module["preRun"].push(runWithFS); // FS is not initialized yet, wait for it
  }

 }
 loadPackage({"files": [{"audio": 0, "start": 0, "crunched": 0, "end": 2473, "filename": "/main.lua"}, {"audio": 0, "start": 2473, "crunched": 0, "end": 2697, "filename": "/conf.lua"}, {"audio": 0, "start": 2697, "crunched": 0, "end": 2961, "filename": "/.git/index"}, {"audio": 0, "start": 2961, "crunched": 0, "end": 3053, "filename": "/.git/FETCH_HEAD"}, {"audio": 0, "start": 3053, "crunched": 0, "end": 3316, "filename": "/.git/config"}, {"audio": 0, "start": 3316, "crunched": 0, "end": 3389, "filename": "/.git/description"}, {"audio": 0, "start": 3389, "crunched": 0, "end": 3430, "filename": "/.git/ORIG_HEAD"}, {"audio": 0, "start": 3430, "crunched": 0, "end": 3453, "filename": "/.git/HEAD"}, {"audio": 0, "start": 3453, "crunched": 0, "end": 3509, "filename": "/.git/COMMIT_EDITMSG"}, {"audio": 0, "start": 3509, "crunched": 0, "end": 3749, "filename": "/.git/info/exclude"}, {"audio": 0, "start": 3749, "crunched": 0, "end": 4201, "filename": "/.git/hooks/applypatch-msg.sample"}, {"audio": 0, "start": 4201, "crunched": 0, "end": 4599, "filename": "/.git/hooks/pre-applypatch.sample"}, {"audio": 0, "start": 4599, "crunched": 0, "end": 4788, "filename": "/.git/hooks/post-update.sample"}, {"audio": 0, "start": 4788, "crunched": 0, "end": 9686, "filename": "/.git/hooks/pre-rebase.sample"}, {"audio": 0, "start": 9686, "crunched": 0, "end": 11038, "filename": "/.git/hooks/pre-push.sample"}, {"audio": 0, "start": 11038, "crunched": 0, "end": 11934, "filename": "/.git/hooks/commit-msg.sample"}, {"audio": 0, "start": 11934, "crunched": 0, "end": 13173, "filename": "/.git/hooks/prepare-commit-msg.sample"}, {"audio": 0, "start": 13173, "crunched": 0, "end": 16784, "filename": "/.git/hooks/update.sample"}, {"audio": 0, "start": 16784, "crunched": 0, "end": 18426, "filename": "/.git/hooks/pre-commit.sample"}, {"audio": 0, "start": 18426, "crunched": 0, "end": 19317, "filename": "/.git/objects/b9/358bd57d7ebbcc29a1eb3799bf9064ded08c88"}, {"audio": 0, "start": 19317, "crunched": 0, "end": 19399, "filename": "/.git/objects/63/78540b7a1c8f8f12fb5deff9ce2d3e097cee91"}, {"audio": 0, "start": 19399, "crunched": 0, "end": 19553, "filename": "/.git/objects/e5/bc6ff9da8c8849f8dc79c07f9756205ae1d77d"}, {"audio": 0, "start": 19553, "crunched": 0, "end": 19635, "filename": "/.git/objects/84/a1900789fc90c580b6d83cddb66bb84d378cf8"}, {"audio": 0, "start": 19635, "crunched": 0, "end": 19716, "filename": "/.git/objects/62/00333fd8f8cf5fe527b525d6e14b15be1de388"}, {"audio": 0, "start": 19716, "crunched": 0, "end": 19798, "filename": "/.git/objects/b4/7b9d48cd2e9a13c929d4c360b838a06c9623e2"}, {"audio": 0, "start": 19798, "crunched": 0, "end": 20001, "filename": "/.git/objects/0e/babc836b666526c47fa0078c50ef7adbf74613"}, {"audio": 0, "start": 20001, "crunched": 0, "end": 20705, "filename": "/.git/objects/87/67219ead9f87772dc016d6b55614575783864b"}, {"audio": 0, "start": 20705, "crunched": 0, "end": 20880, "filename": "/.git/objects/78/728f8f2bd6e8bffff32934177bab5f582d53c9"}, {"audio": 0, "start": 20880, "crunched": 0, "end": 21036, "filename": "/.git/objects/7c/dacb0e84b9fec3269553259fc211d7642f59a0"}, {"audio": 0, "start": 21036, "crunched": 0, "end": 21158, "filename": "/.git/objects/9f/1dde45907bb37fcaf48b7ad827692d9ab641fd"}, {"audio": 0, "start": 21158, "crunched": 0, "end": 21203, "filename": "/.git/objects/06/c44a875c9f7599e2fe5f4067ffba2548a284ec"}, {"audio": 0, "start": 21203, "crunched": 0, "end": 21319, "filename": "/.git/objects/42/7209e792a88c93e082e86465a644f49dc10a33"}, {"audio": 0, "start": 21319, "crunched": 0, "end": 21784, "filename": "/.git/objects/96/512b4b0310f4efcd690158bba2d0ad7c4a695a"}, {"audio": 0, "start": 21784, "crunched": 0, "end": 21938, "filename": "/.git/objects/1c/44a0fe38f109113b25f7db2caf29746883b7ec"}, {"audio": 0, "start": 21938, "crunched": 0, "end": 22137, "filename": "/.git/objects/e4/6a0e35a9c221e1f42734f0de0541c152846c38"}, {"audio": 0, "start": 22137, "crunched": 0, "end": 91589, "filename": "/.git/objects/75/53c370c17cd3b6c208eead5f1f5b5f6843f03b"}, {"audio": 0, "start": 91589, "crunched": 0, "end": 91772, "filename": "/.git/objects/14/db2a723f22344a48d12813d78def8a59b3c782"}, {"audio": 0, "start": 91772, "crunched": 0, "end": 92441, "filename": "/.git/objects/da/1d196b46b2e3dfd1f921f870f0dd2af41f6d09"}, {"audio": 0, "start": 92441, "crunched": 0, "end": 92494, "filename": "/.git/objects/5f/c97b3bcfbab3f7196bbe5d2750afd11e12c3a7"}, {"audio": 0, "start": 92494, "crunched": 0, "end": 92535, "filename": "/.git/refs/heads/master"}, {"audio": 0, "start": 92535, "crunched": 0, "end": 92576, "filename": "/.git/refs/remotes/origin/master"}, {"audio": 0, "start": 92576, "crunched": 0, "end": 93067, "filename": "/.git/logs/HEAD"}, {"audio": 0, "start": 93067, "crunched": 0, "end": 93558, "filename": "/.git/logs/refs/heads/master"}, {"audio": 0, "start": 93558, "crunched": 0, "end": 93982, "filename": "/.git/logs/refs/remotes/origin/master"}, {"audio": 0, "start": 93982, "crunched": 0, "end": 170564, "filename": "/assets/img/mapa.jpg"}], "remote_package_size": 170564, "package_uuid": "8b958980-d100-434e-a3ae-b1f7d25a701b"});

})();
