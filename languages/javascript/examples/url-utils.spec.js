import expect from 'expect';
import { queryString, urlWithQuery, getProtocolRelativeOrigin } from './../../../src/shared/util/url-utils';

describe('The url-utils module', () => {
    describe('queryString', () => {
        it('returns URL encoded key value pairs separated by ampersand', () => {
            expect(queryString({ foo: 1, bar: true, baz: 'foo bar' })).toEqual('foo=1&bar=true&baz=foo%20bar');
        });

        it('skips keys with null/undefined values', () => {
            expect(queryString({ foo: 1, bar: null, baz: undefined })).toEqual('foo=1');
        });

        it('returns empty string for null/undefined', () => {
            expect(queryString(null)).toEqual('');
            expect(queryString(undefined)).toEqual('');
        });
    });

    describe('urlWithQuery', () => {
        it('can take a query object or string and concatenate with ?', () => {
            expect(urlWithQuery('http://www.example.com', {foo: 1, bar: 'a b'})).toEqual('http://www.example.com?foo=1&bar=a%20b')
            expect(urlWithQuery('http://www.example.com', queryString({foo: 1, bar: 'a b'}))).toEqual('http://www.example.com?foo=1&bar=a%20b')
        });

        it('can take a query object or string and concatenate with &', () => {
            expect(urlWithQuery('http://www.example.com?baz=2', {foo: 1, bar: 'a b'})).toEqual('http://www.example.com?baz=2&foo=1&bar=a%20b')
            expect(urlWithQuery('http://www.example.com?baz=2', queryString({foo: 1, bar: 'a b'}))).toEqual('http://www.example.com?baz=2&foo=1&bar=a%20b')
        });
    });

    describe('getProtocolRelativeOrigin', () => {
        it('returns empty string for falsy url', () => {
            const result = getProtocolRelativeOrigin(null);
            expect(result).toBe('');
        });

        it('returns empty string for url without origin', () => {
            const result = getProtocolRelativeOrigin('/example.html');
            expect(result).toBe('');
        });

        it('returns origin without http protocol', () => {
            const result = getProtocolRelativeOrigin('http://www.example.com');
            expect(result).toBe('//www.example.com');
        });

        it('returns origin without https protocol', () => {
            const result = getProtocolRelativeOrigin('https://www.example.com');
            expect(result).toBe('//www.example.com');
        });

        it('returns origin on already protocol relative url', () => {
            const result = getProtocolRelativeOrigin('//www.example.com');
            expect(result).toBe('//www.example.com');
        });

        it('returns origin from url with sub path', () => {
            const result = getProtocolRelativeOrigin('http://www.example.com/example/example.com');
            expect(result).toBe('//www.example.com');
        });

    });
});
