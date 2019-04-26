export function queryString(query) {
    const notNullEntries = Object.entries(query || {}).filter(([_, v]) => v != null);
    const encodeEntry = ([k, v]) => [k, v].map(encodeURIComponent).join('=');
    return notNullEntries.map(encodeEntry).join('&');
}

export function urlWithQuery(url, query) {
    const _queryString = (typeof query === 'string' ? query : queryString(query));
    if (_queryString) {
        const sep = (url.includes('?') ? '&' : '?');
        return url + sep + _queryString;
    } else {
        return url;
    }
}

export function getProtocolRelativeOrigin(url = '') {
    const match = url && url.match(/\/\/[^\/]+/);
    return match && match[0] || '';
}
