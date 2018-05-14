export default {
  data () {
    let lang = window.navigator.language
    if (lang.indexOf('-') !== -1) lang = lang.split('-')[0]
    if (lang.indexOf('_') !== -1) lang = lang.split('_')[0]
    return {
      apiURL: 'http://162.243.216.13:69',
      lang
    }
  },
  methods: {
    isDataNull (v) {
      return v === undefined || v == null || v.length <= 0
    }
  }
}
